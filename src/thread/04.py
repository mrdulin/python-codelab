import time
import threading


def test():
    time.sleep(5)
    for i in range(1, 10):
        print(i)


thread1 = threading.Thread(target=test)
thread1.start()
thread1.join()
print('主线程完成了')
