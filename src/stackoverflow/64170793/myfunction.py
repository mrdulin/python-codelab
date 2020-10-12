import myclass


def my_function():
    a = myclass.MyClass('a', 3)
    b = myclass.MyClass('b', 4)
    print('a:\n', a)
    print('b:\n', b)
    print('a and b are different instances of MyClass:', a != b)
    return a.get_value() + b.get_value()
