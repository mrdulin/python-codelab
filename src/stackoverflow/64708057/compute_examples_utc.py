from compute_examples import Compute
import unittest


class Test(unittest.TestCase):
    obj_compute_examples = Compute()

    def test_0_add(self):
        print("Start add test\n")

        self.assertEqual(self.obj_compute_examples.add(2, 2), 4)
