import random
import unittest
import unittest.mock as mock
import learning


class TestLearning(unittest.TestCase):

    def test_get_random_belief_bit(self):
        with mock.patch('random.uniform', mock.Mock()) as mock_uniform:
            mock_uniform.return_value = 0
            bit = learning.get_random_belief_bit(0.4)
            self.assertEqual(bit, 0)
            mock_uniform.assert_called_once()


if __name__ == '__main__':
    unittest.main()
