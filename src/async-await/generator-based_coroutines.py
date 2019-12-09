
import asyncio


@asyncio.coroutine
def get_data():
    return 'data'


@asyncio.coroutine
def old_style_coroutine():
    print('hello')
    yield from asyncio.sleep(1)
    print('world')
    return (yield from get_data())


async def main():
    res = await old_style_coroutine()
    print(res)

asyncio.run(main())
