import asyncio
import aiohttp


async def fetch_page(session, url):
    async with session.get(url) as response:
        return response


async def main():
    urls = (
        'https://jsonplaceholder.typicode.com/todos/1',
        'https://jsonplaceholder.typicode.com/todos/2',
        'https://jsonplaceholder.typicode.com/todos/3',
        'https://jsonplaceholder.typicode.com/todos/4',
        'https://jsonplaceholder.typicode.com/todos/5'
    )
    session = aiohttp.ClientSession()
    tasks = map(lambda x: fetch_page(session, x), urls)
    done, pending = await asyncio.wait(tasks, timeout=120)

    for future in done:
        response = future.result()
        print('done response:', response)
    for future in pending:
        print('pending future:', future)

    await session.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
