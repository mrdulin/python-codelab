class MyContextManager:
    def __enter__(self):
        print('entering...')

    def __exit__(self, exception_type, execption_value, traceback):
        print('leaving...')

        if exception_type is None:
            print('No exception!')
            return True
        elif exception_type is ValueError:
            print('value error!!')
            return True
        else:
            print('other error')
            return True


with MyContextManager():
    print('Testing...')
    raise(ValueError)

print('\n')
with MyContextManager():
    print('Testing 2...')
