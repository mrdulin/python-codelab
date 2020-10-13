from arg import ToBeMocked


class A():
    def __init__(self, arg=ToBeMocked()):
        self.arg = arg
