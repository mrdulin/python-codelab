def do(url):
    try:
        check(url)
        foo(url)
    except:
        bar(url)


def check(url):
    if ' ' in url:
        raise Exception('oops')


def foo(url):
    pass


def bar(url):
    pass
