from code2 import Bar


class Foo:
    bar_instance = Bar(init1='nothing', init2='nothing')

    @classmethod
    def foo_method(cls):
        Foo.bar_instance.bar_method()
