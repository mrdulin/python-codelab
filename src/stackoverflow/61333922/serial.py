class Serial(object):
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate

    def write(self, data):
        return 100
