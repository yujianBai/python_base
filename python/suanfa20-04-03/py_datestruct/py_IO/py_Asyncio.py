#auth Bernard
#date 2020-04-20

""" Asyncio
基于协程实现的内置并发网络库
    python3引入到内置库， 协程+ 事件循环
    生态不完善， 没有大规模生产环境检测
    使用不广泛
"""

import asyncio
from aiohttp import ClientSession

async def fetchurl,,session::
    async with session.get(url) as response:
        return await response.read()

async def run(r=10):
    url = "http://httpbin.org/get"
    tasks = []

    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch(url, session))
            task.append(task)
        response = await asyncio.gather(*tasks)
        for resp_body in response:
            print(resp_body)

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run())
loop.run_until_complete(future)
