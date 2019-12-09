import time
import asyncio


start = time.time()


def tic():
    return 'at %1.1f seconds' % (time.time() - start)


async def task1():
    print('task1 started work: {}'.format(tic()))
    await asyncio.sleep(2)
    print('task1 ended work{}'.format(tic()))


async def task2():
    print('task2 started work: {}'.format(tic()))
    await asyncio.sleep(2)
    print('task2 ended work{}'.format(tic()))


async def task3():
    print('task3 started work: {}'.format(tic()))
    await asyncio.sleep(1)
    print('task3 ended work{}'.format(tic()))


ioloop = asyncio.get_event_loop()

tasks = [
    ioloop.create_task(task1()),
    ioloop.create_task(task2()),
    ioloop.create_task(task3())
]

ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()
