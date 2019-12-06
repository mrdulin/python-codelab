class UserDefinedException(Exception):
    def __init__(self, eid, message):
        self.eid = eid
        self.message = message


class ExceptionDemo:
    def draw(self, number):
        print('called compute(%s)' % str(number))
        if number > 500 or number <= 0:
            raise UserDefinedException(101, 'number out of bound')
        else:
            print('normal exit')


demo = ExceptionDemo()

try:
    demo.draw(125)
    demo.draw(900)
except UserDefinedException as e:
    print('Exception caught: id: {}, message: {}'.format(e.eid, e.message))
