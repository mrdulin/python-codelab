import os


def foo():
    sum = 0
    for i in range(10000):
        sum += i
    return sum


if __name__ == '__main__':
    import cProfile
    filename = os.path.dirname(__file__) + '/foo3_prof.txt'
    cProfile.run('foo()', filename=filename)
    import pstats
    p = pstats.Stats(filename)
    p.sort_stats('time').print_stats()
