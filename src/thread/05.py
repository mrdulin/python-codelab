import time
import threading


def test():
    time.sleep(5)
    for i in range(1, 10):
        print(i)


thread1 = threading.Thread(target=test)
print('1.当前线程是否是活动的:', thread1.isAlive())
thread1.start()
print('2.当前线程是否是活动的:', thread1.isAlive())
print('当前线程的名称:', thread1.getName())
thread1.join()

print('主线程完成')