from init_test import InitTest


class TestA(InitTest):
    def test_foo(self):
        self.assertEqual(self.user, {'id': '1'})
