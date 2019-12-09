from multiprocessing import Process, Lock
import os


def f_without_lock(_, i):
    print(f'pid: {os.getpid()} hello world {i}')


def f(l, i):
    l.acquire()
    try:
        print(f'pid: {os.getpid()} hello world {i}')
    finally:
        l.release()


if __name__ == '__main__':
    lock = Lock()
    for num in range(10):
        Process(target=f_without_lock, args=(lock, num)).start()

## 加锁进行进程间数据同步 ##

# Output 1

# pid: 42411 hello world 1
# pid: 42410 hello world 0
# pid: 42412 hello world 2
# pid: 42413 hello world 3
# pid: 42414 hello world 4
# pid: 42415 hello world 5
# pid: 42416 hello world 6
# pid: 42417 hello world 7
# pid: 42418 hello world 8
# pid: 42419 hello world 9

# Output 2

# pid: 42676 hello world 0
# pid: 42677 hello world 1
# pid: 42678 hello world 2
# pid: 42680 hello world 4
# pid: 42679 hello world 3
# pid: 42681 hello world 5
# pid: 42682 hello world 6
# pid: 42683 hello world 7
# pid: 42685 hello world 8
# pid: 42686 hello world 9

# 加了锁以后，进程id和num的值都是从小到大，一一对应的


## 不加锁 ##

# Output 1

# TODO
