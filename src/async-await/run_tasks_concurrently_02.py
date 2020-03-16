import asyncio


async def request(url):
    if url == 'a':
        print('request a')
        raise Exception('request a fail')
    elif url == 'b':
        print('request b')
        return 'b response'
    elif url == 'c':
        print('request c')
        return 'c response'


async def main(return_exceptions=False):
    tasks = request('a'), request('b'), request('c'),
    try:
        return await asyncio.gather(
            *tasks,
            return_exceptions=return_exceptions
        )
    except Exception as identifier:
        print(identifier)


loop = asyncio.get_event_loop()
resultWithReturnException = loop.run_until_complete(main(return_exceptions=True))
print('resultWithReturnException:', resultWithReturnException)
# resultWithReturnException: [Exception('request a fail'), 'b response', 'c response']
resultWithoutReturnException = loop.run_until_complete(main(return_exceptions=False))
print('resultWithoutReturnException:', resultWithoutReturnException)
# resultWithoutReturnException: None

loop.close()
