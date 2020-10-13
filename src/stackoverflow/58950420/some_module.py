class SomeModule():
    def a(): pass
    def b(): pass
    def c(): pass

    @classmethod
    def bring_them_altogether(cls):
        cls.a()
        cls.b()
        cls.c()
