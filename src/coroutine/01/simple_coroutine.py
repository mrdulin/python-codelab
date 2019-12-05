
def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received: ', x)


my_coro = simple_coroutine()
print(my_coro)

# "预激"(prime)协程（即，让协程向前执行到第一个yield表达式，准备好作为活跃的协程使用）
next(my_coro)
my_coro.send(42)
