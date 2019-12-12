import unittest
from test_base import TestBaseImporter
from test_child import TestChildImporter

if __name__ == '__main__':
    test_loader = unittest.TestLoader()

    test_classes_to_run = [TestBaseImporter, TestChildImporter]
    suites_list = []
    for test_class in test_classes_to_run:
        suite = test_loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)
    unittest.TextTestRunner().run(big_suite)
