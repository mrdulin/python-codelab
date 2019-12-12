import unittest
from test_a import TestA
from test_b import TestB


if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    test_classes = [TestA, TestB]

    suites = []
    for test_class in test_classes:
        suite = test_loader.loadTestsFromTestCase(test_class)
        suites.append(suite)

    big_suite = unittest.TestSuite(suites)
    unittest.TextTestRunner().run(big_suite)
