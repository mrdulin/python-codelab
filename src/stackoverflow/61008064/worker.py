from helper import Helper


class Worker:
    def __init__(self):
        self.helper = Helper('db')

    def work(self):
        path = self.helper.get_path()
        print(f'Working on {path}')
        return path
