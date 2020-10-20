def foo(i):
    if i == 'this':
        return 'a'
    else:
        return 'b'


def bar(items):
    results = []
    for item in items:
        results.append(foo(item))
    return results
