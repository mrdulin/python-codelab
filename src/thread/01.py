import threading


def test(x, y):
    for i in range(x, y):
        print(i)


thread1 = threading.Thread(name='t1', target=test, args=(1, 10))
thread2 = threading.Thread(name='t2', target=test, args=(11, 20))

thread1.start()
thread2.start()
