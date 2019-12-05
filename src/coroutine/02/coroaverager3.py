import unittest
from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    """子生成器

    Returns:
        [type] -- [description]
    """
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


def grouper(results, key):
    """委派生成器"""
    while True:
        results[key] = yield from averager()


def main(data):
    """客户端代码，即调用方"""
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    # print(results)
    report(results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(':')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit))


if __name__ == '__main__':
    data = {
        'girls:kg': [40.9, 38.5, 44.3],
        'girls:m': [1.6, 1.51, 1.4],
        'boys:kg': [39.0, 40.8, 43.2],
        'boys:m': [1.38, 1.5, 1.32]
    }
    main(data)
