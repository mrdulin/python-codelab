class LookingGlass:
    def __enter__(self):
        import sys
        self.original_value = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_value(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        """如果一切正常，Python调用__exit__方法时传入的参数是None, None, None;
        如果抛出了异常，这三个参数是异常数据

        重复导入模块不会消耗很多资源，因为Python会缓存导入的模块

        Arguments:
            exc_type {[type]} -- [异常类（例如ZeroDivisionError）]
            exc_value {[type]} -- [异常实例]
            traceback {[type]} -- [traceback对象]

        Returns:
            [type] -- [返回True, 告诉解释器，异常已经处理了。如果__exit__方法返回None, 或者True以外的值，with块中的任何异常都会向上冒泡]
        """
        import sys
        sys.stdout.write = self.original_value
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True
