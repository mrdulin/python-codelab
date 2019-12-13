def foo():
    sum = 0
    for i in range(10000):
        sum += i
    return sum


if __name__ == '__main__':
    foo()

#  python3 -m cProfile /Users/ldu020/workspace/github.com/mrdulin/python-codelab/src/performance-optimization/cProfile/foo.py
