import contextlib
@contextlib.contextmanager
def looking_glass():
    import sys
    origin_write = sys.stdout.write

    def reverse_write(text):
        origin_write(text[::-1])
    sys.stdout.write = reverse_write

    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = origin_write
        if msg:
            print(msg)


with looking_glass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)
    print(1/0)

print(what)
print('Back to normal')
