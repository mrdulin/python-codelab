class MyClass(object):
    def __init__(self, name, value):
        self._name = name
        self._value = value

    def get_value(self):
        return self._value
