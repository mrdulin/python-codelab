
import asyncio


@asyncio.coroutine
def old_style_coroutine():
    print('hello')
    yield from asyncio.sleep(1)
    print('world')


async def main():
    await old_style_coroutine()

asyncio.run(main())
