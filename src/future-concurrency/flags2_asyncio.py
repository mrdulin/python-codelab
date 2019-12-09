import asyncio
import collections
import aiohttp
from aiohttp import web
import tqdm
from aiohttp.http import HttpProcessingError


async def get_flag(session, base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    async with session.get(url) as response:
        if response.status == 200:
            image = await response.read()
            return image
        elif response.status == 404:
            raise web.HTTPNotFound()
        else:
            raise HttpProcessingError(
                code=response.status, message=response.reason, headers=response.headers)
# TODO
