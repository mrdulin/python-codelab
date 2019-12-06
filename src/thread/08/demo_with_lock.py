import threading
import time

lock = threading.RLock()


class Counter:
    count = 0

    def increment(self, thread_name):
        self.count += 1
        print('%s:%d' % (thread_name, self.count))

    def getCount(self):
        return self.count


class CountingThread(threading.Thread):
    def __init__(self, counter):
        super(CountingThread, self).__init__()
        self.counter = counter

    def run(self):
        lock.acquire()
        for i in range(100):
            self.counter.increment(self.name)
        lock.release()


counter = Counter()
t_list = []
t_list.append(CountingThread(counter))
t_list.append(CountingThread(counter))
for t in t_list:
    t.start()
    t.join()
print(counter.getCount())
