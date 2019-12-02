import threading


class mythread(threading.Thread):
    def run(self):
        for i in range(1, 10):
            print(i)


thread1 = mythread()
thread2 = mythread()

# thread1.start()
# thread2.start()

thread1.run()
thread2.run()