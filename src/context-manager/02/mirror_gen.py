import contextlib
@contextlib.contextmanager
def looking_glass():
    import sys
    origin_write = sys.stdout.write

    def reverse_write(text):
        origin_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = origin_write


with looking_glass() as what2:
    print('Alice, Kitty and Snowdrop')
    print(what2)

print(what2)
print('Back to normal')
