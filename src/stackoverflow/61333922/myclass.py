import serial


class MyClass(object):

    def __init__(self, com_port, baudrate):
        self.sp = serial.Serial(com_port, baudrate)

    def do_something(self, data):
        num_bytes_written = self.sp.write(data)
        if num_bytes_written != len(data):
            return -1
        return 0
