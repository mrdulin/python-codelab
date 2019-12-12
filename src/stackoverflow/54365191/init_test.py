import unittest


class InitTest(unittest.TestCase):
    def setUp(self):
        self.user = {'id': '1'}

    def tearDown(self):
        self.user = None
