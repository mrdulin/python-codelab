import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """test name_function.py"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('lin', 'du')
        self.assertEqual(formatted_name, 'Lin Du')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('mr', 'lin', 'du')
        self.assertEqual(formatted_name, 'Mr Du Lin')


unittest.main()
