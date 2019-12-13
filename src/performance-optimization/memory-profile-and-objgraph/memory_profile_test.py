from memory_profiler import profile


@profile
def fibonacci(n):
    if n < 0:
        return -1
    elif n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    fibonacci(10)

#  python3 -m memory_profiler /Users/ldu020/workspace/github.com/mrdulin/python-codelab/src/performance-optimization/memory-profile-and-objgraph/memory_profile_test.py
