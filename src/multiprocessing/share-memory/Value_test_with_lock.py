import time
from multiprocessing import Process, Value


def func(val):
    """多进程修改共享的数据，
    Output: 100
    是进程安全的

    Arguments:
        val {[type]} -- [description]
    """
    for i in range(10):
        time.sleep(0.1)
        with val.get_lock():
            val.value += 1


if __name__ == '__main__':
    v = Value('i', 0)
    process_list = [Process(target=func, args=(v,)) for i in range(10)]
    for p in process_list:
        p.start()
    for p in process_list:
        p.join()
    print(v.value)
