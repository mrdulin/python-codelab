import threading
import time


class Counter:
    count = 0

    def increment(self, thread_name):
        self.count += 1
        # print('%s:%d' % (thread_name, self.count))

    def getCount(self):
        return self.count


class CountingThread(threading.Thread):
    def __init__(self, counter):
        super(CountingThread, self).__init__()
        self.counter = counter

    def run(self):
        for i in range(100):
            self.counter.increment(self.name)
            print('getCount, %s: %d' % (self.name, self.counter.getCount()))


counter = Counter()
t1 = CountingThread(counter)
t2 = CountingThread(counter)
t1.start()
t2.start()
t1.join()
t2.join()
print(counter.getCount())
