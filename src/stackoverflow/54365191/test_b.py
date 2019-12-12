from init_test import InitTest


class TestB(InitTest):
    def test_bar(self):
        self.assertEqual(self.user, {'id': '1'})
