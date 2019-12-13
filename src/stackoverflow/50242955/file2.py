import file1


class MyClass():
    @classmethod
    def calculate(cls):
        x = 1
        inst = file1.SomeHelper()
        if x > inst.my_var:
            return True
        return False
