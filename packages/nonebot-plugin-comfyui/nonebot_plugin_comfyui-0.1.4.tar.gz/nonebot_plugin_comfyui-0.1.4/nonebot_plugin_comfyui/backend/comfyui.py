import copy
import json
import random
import uuid
import base64

import aiofiles
import aiohttp
import asyncio

from tqdm import tqdm
from nonebot import logger
from nonebot.adapters import Event
from typing import Union, Optional
from argparse import Namespace

from ..config import config


class ComfyuiUI:

    def __init__(
            self,
            nb_event: Event,
            args: Namespace,
            prompt: str = None,
            negative_prompt: str = None,
            accept_ratio: str = None,
            seed: Optional[int] = None,
            steps: Optional[int] = None,
            cfg_scale: Optional[float] = None,
            denoise_strength: Optional[float] = None,
            height: Optional[int] = None,
            width: Optional[int] = None,
            video: Optional[bool] = None,
            work_flows: str = None,
            sampler: Optional[str] = None,
            scheduler: Optional[str] = None,
            batch_size: Optional[int] = None,
            model: Optional[str] = None,
            **kwargs
    ):

        # 映射参数相关
        self.reflex_dict = {'sampler': {
            "DPM++ 2M": "dpmpp_2m",
            "DPM++ SDE": "dpmpp_sde",
            "DPM++ 2M SDE": "dpmpp_2m_sde",
            "DPM++ 2M SDE Heun": "dpmpp_2m_sde",
            "DPM++ 2S a": "dpmpp_2s_ancestral",
            "DPM++ 3M SDE": "dpmpp_3m_sde",
            "Euler a": "euler_ancestral",
            "Euler": "euler",
            "LMS": "lms",
            "Heun": "heun",
            "DPM2": "dpm_2",
            "DPM2 a": "dpm_2_ancestral",
            "DPM fast": "dpm_fast",
            "DPM adaptive": "dpm_adaptive",
            "Restart": "restart",
            "HeunPP2": "heunpp2",
            "IPNDM": "ipndm",
            "IPNDM_V": "ipndm_v",
            "DEIS": "deis",
            "DDIM": "ddim",
            "DDIM CFG++": "ddim",
            "PLMS": "plms",
            "UniPC": "uni_pc",
            "LCM": "lcm",
            "DDPM": "ddpm",
        }, 'scheduler': {
            "Automatic": "normal",
            "Karras": "karras",
            "Exponential": "exponential",
            "SGM Uniform": "sgm_uniform",
            "Simple": "simple",
            "Normal": "normal",
            "DDIM": "ddim_uniform",
            "Beta": "beta"
        }
        }

        # 必要参数
        self.nb_event = nb_event
        self.args = args

        # 绘图参数相关
        self.prompt: str = self.list_to_str(prompt or "")
        self.negative_prompt: str = self.list_to_str(negative_prompt or "")
        self.accept_ratio: str = accept_ratio
        if self.accept_ratio is None:
            self.height: int = height or 1024
            self.width: int = width or 1024
        else:
            self.width, self.height = self.extract_ratio()
        self.seed: int = seed or random.randint(0, 2 ^ 32)
        self.steps: int = steps or 20
        self.cfg_scale: float = cfg_scale or 7.0
        self.denoise_strength: float = denoise_strength or 1.0
        self.video: bool = video or False

        self.sampler: str = (
            self.reflex_dict['sampler'].get(sampler, "dpmpp_2m") if
            sampler not in self.reflex_dict['sampler'].values() else
            sampler or "dpmpp_2m"
        )
        self.scheduler: str = (
            self.reflex_dict['scheduler'].get(scheduler, "normal") if
            scheduler not in self.reflex_dict['scheduler'].values() else
            scheduler or "normal"
        )

        self.batch_size: int = batch_size or 1
        self.model: str = model or config.comfyui_model

        # ComfyuiAPI相关
        self.work_flows: str = work_flows or "txt2img"
        logger.info(f"选择工作流: {self.work_flows}")
        self.api_json = None
        self.reflex_json = None
        self.backend_url: str = config.comfyui_url

        # 用户相关
        self.client_id = uuid.uuid4().hex
        self.user_id = self.nb_event.get_user_id()
        self.task_id = None

        # 图片相关
        self.init_images: list[str] = []
        self.image_url: list = []
        self.image_byte: list[bytes] = []

    async def get_workflows_json(self):
        async with aiofiles.open(
                f"{config.comfyui_workflows_dir}/{self.work_flows}.json",
                'r',
                encoding='utf-8'
        ) as f:
            self.api_json = json.loads(await f.read())

        async with aiofiles.open(
                f"{config.comfyui_workflows_dir}/{self.work_flows}_reflex.json",
                'r',
                encoding='utf-8'
        ) as f:
            self.reflex_json = json.loads(await f.read())

    def extract_ratio(self, max_res=None):
        """
        提取宽高比为分辨率
        """

        if ":" in self.accept_ratio:
            width_ratio, height_ratio = map(int, self.accept_ratio.split(':'))
        else:
            return 768, 1152

        max_resolution = config.comfyui_base_res
        aspect_ratio = width_ratio / height_ratio
        if aspect_ratio >= 1:
            width = int(min(max_resolution, max_resolution))
            height = int(width / aspect_ratio)
        else:
            height = int(min(max_resolution, max_resolution))
            width = int(height * aspect_ratio)

        return width, height

    def update_api_json(self, init_images):
        api_json = copy.deepcopy(self.api_json)

        update_mapping = {
            "sampler": {
                "seed": self.seed,
                "steps": self.steps,
                "cfg": self.cfg_scale,
                "sampler_name": self.sampler,
                "scheduler": self.scheduler,
                "denoise": self.denoise_strength
            },
            "seed": {
                "seed": self.seed
            },
            "image_size": {
                "width": self.width,
                "height": self.height,
                "batch_size": self.batch_size
            },
            "prompt": {
                "text": self.prompt
            },
            "negative_prompt": {
                "text": self.negative_prompt
            },
            "checkpoint": {
                "ckpt_name": self.model if self.model else None
            },
            "load_image": {
                "image": init_images[0]['name'] if self.init_images else None
            },
            "tipo": {
                "width": self.width,
                "height": self.height,
                "seed": self.seed,
                "tags": self.prompt,
            }
        }

        __OVERRIDE_SUPPORT_KEYS__ = {'keep', 'append_prompt', 'append_negative_prompt', 'remove', "randint"}
        __ALL_SUPPORT_NODE__ = set(update_mapping.keys())

        for item, node_id in self.reflex_json.items():

            if node_id:
                if isinstance(node_id, dict):
                    temp_dict = copy.deepcopy(update_mapping)
                    for node, override_dict in node_id.items():
                        single_node_or = override_dict.get("override", {})

                        for key, override_action in single_node_or.items():

                            if override_action == "randint":
                                temp_dict[item][key] = random.randint(0, 99999)

                            elif override_action == "keep":
                                continue

                            elif override_action == "append_prompt":
                                prompt = api_json[node]['inputs'][key]
                                prompt = self.prompt + prompt
                                api_json[node]['inputs'][key] = prompt

                            elif override_action == "append_negative_prompt":
                                prompt = api_json[node]['inputs'][key]
                                prompt = self.negative_prompt + prompt
                                api_json[node]['inputs'][key] = prompt

                else:
                    node_id = [str(node_id)] if isinstance(node_id, int) else node_id

                    for id_ in node_id:
                        update_dict = api_json.get(id_, None)
                        if update_dict and item in update_mapping:
                            api_json[id_]['inputs'].update(update_mapping[item])

        self.compare_dicts(api_json, self.api_json)
        self.api_json = api_json

    async def heart_beat(self, id_):
        logger.info(f"{id_} 开始请求")

        async def get_images():

            response = await self.http_request(
                method="GET",
                target_url=f"{self.backend_url}/history/{id_}",
            )

            if response:
                for img in response[id_]['outputs'][str(self.reflex_json.get('output', 9))]['images']:
                    img_url = f"{self.backend_url}/view?filename={img['filename']}"
                    self.image_url.append(img_url)

        async with aiohttp.ClientSession() as session:
            ws_url = f'{self.backend_url}/ws?clientId={self.client_id}'
            async with session.ws_connect(ws_url) as ws:

                logger.info(f"WS连接成功: {ws_url}")
                progress_bar = None

                async for msg in ws:
                    if msg.type == aiohttp.WSMsgType.TEXT:
                        ws_msg = json.loads(msg.data)

                        if ws_msg['type'] == 'progress':
                            value = ws_msg['data']['value']
                            max_value = ws_msg['data']['max']

                            if progress_bar is None:
                                progress_bar = await asyncio.to_thread(
                                    tqdm, total=max_value,
                                   desc=f"Prompt ID: {ws_msg['data']['prompt_id']}",
                                   unit="steps"
                                )

                            delta = value - progress_bar.n
                            await asyncio.to_thread(progress_bar.update, delta)

                        if ws_msg['type'] == 'executing':
                            if ws_msg['data']['node'] is None:
                                logger.info(f"{id_}绘画完成!")
                                await get_images()
                                await ws.close()

                    elif msg.type == aiohttp.WSMsgType.ERROR:
                        logger.error(f"Error: {msg.data}")
                        await ws.close()
                        break

                if progress_bar is not None:
                    await asyncio.to_thread(progress_bar.close)

    async def posting(self):

        await self.get_workflows_json()

        upload_img_resp_list = []

        if self.init_images:
            for image in self.init_images:
                resp = await self.upload_image(image, uuid.uuid4().hex)
                upload_img_resp_list.append(resp)

        self.update_api_json(upload_img_resp_list)

        input_ = {
            "client_id": self.client_id,
            "prompt": self.api_json
        }

        respone = await self.http_request(
            method="POST",
            target_url=f"{self.backend_url}/prompt",
            content=json.dumps(input_)
        )

        if respone.get("error", None):
            logger.error(respone)
            raise RuntimeError(respone["status_code"])

        self.task_id = respone['prompt_id']

        await self.heart_beat(self.task_id)
        await self.download_img()

    @staticmethod
    async def http_request(
            method,
            target_url,
            headers=None,
            params=None,
            content=None,
            format=True,
            timeout=5000,
            verify=True,
            proxy=False
    ) -> Union[dict, bytes]:

        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout)) as session:
            async with session.request(
                    method,
                    target_url,
                    headers=headers,
                    params=params,
                    data=content,
                    ssl=verify,
            ) as response:
                if format:
                    return await response.json()
                else:
                    return await response.read()

    async def upload_image(self, image_data: bytes, name, image_type="input", overwrite=False):

        data = aiohttp.FormData()
        data.add_field('image', image_data, filename=f"{name}.png", content_type=f'image/png')
        data.add_field('type', image_type)
        data.add_field('overwrite', str(overwrite).lower())

        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.backend_url}/upload/image", data=data) as response:
                return json.loads(await response.read())

    async def download_img(self):

        for url in self.image_url:
            response = await self.http_request(
                method="GET",
                target_url=url,
                format=False
            )

            logger.info(f"图片: {url}下载成功")

            self.image_byte.append(response)

    @staticmethod
    def list_to_str(tags_list):
        tags: str = ("".join([i+" " for i in tags_list if isinstance(i,str)])).split(",")
        return ','.join(tags)

    @staticmethod
    def compare_dicts(dict1, dict2):

        modified_keys = {k for k in dict1.keys() & dict2.keys() if dict1[k] != dict2[k]}
        for key in modified_keys:
            logger.info(f"API请求值映射: {key} -> {dict1[key]} -> {dict2[key]}")

