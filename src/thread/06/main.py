import threading
import time

x = 0
lock = threading.RLock()


class mythread(threading.Thread):
    def run(self):
        time.sleep(10)
        global x
        lock.acquire()
        x += 10
        print('%s: %d' % (self.name, x))
        lock.release()


thread_list = []

for i in range(10):
    thread_list.append(mythread())
for thread in thread_list:
    thread.start()
