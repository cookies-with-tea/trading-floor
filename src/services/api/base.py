from typing import Any, Coroutine

import aiohttp
from aiohttp import ClientResponse


class API:
    def __init__(self, base_url: str, suffix: str = '/api/v1') -> None:
        self.session = aiohttp.ClientSession(base_url=base_url)
        self.suffix = suffix

    async def get(self, url: str, **kwargs) -> dict:
        async with self.session.get(self.suffix + url, params=kwargs) as response:
            return await response.json()

    async def post(self, url: str, data: dict) -> ClientResponse:
        async with self.session.post(self.suffix + url, json=data) as response:
            return response
