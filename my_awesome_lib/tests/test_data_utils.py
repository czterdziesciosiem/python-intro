# tests/test_data_utils.py
import unittest
from my_awesome_lib.data_utils import convert_to_celsius, flatten_list

class TestDataUtils(unittest.TestCase):

    def test_convert_to_celsius(self):
        self.assertAlmostEqual(convert_to_celsius(32), 0)
        self.assertAlmostEqual(convert_to_celsius(212), 100)

    def test_flatten_list(self):
        self.assertEqual(flatten_list([1, [2, 3], [4, [5]]]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
 
