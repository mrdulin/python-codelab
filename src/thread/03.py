import time
import threading


def test():
    time.sleep(10)
    for i in range(1, 10):
        print(i)


thread1 = threading.Thread(target=test, daemon=False)
# thread1 = threading.Thread(target=test, daemon=True)
thread1.start()

print('主线程完成了')
