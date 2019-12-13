from multiprocessing import Process, Manager


def f(ns, x, y):
    x.append(1)
    y.append('a')
    ns.x = x
    ns.y = y


if __name__ == '__main__':
    manager = Manager()
    ns = manager.Namespace()
    ns.x = []
    ns.y = []
    print('before process operation: ', ns)
    p = Process(target=f, args=(ns, ns.x, ns.y,))
    p.start()
    p.join()
    print('after process operation: ', ns)
