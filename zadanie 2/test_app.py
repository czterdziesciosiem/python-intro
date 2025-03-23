import unittest
from app import is_valid_email, calculate_area, sort_numbers, format_date, is_palindrome

class TestFunctions(unittest.TestCase):

    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("invalid-email"))

    def test_calculate_area(self):
        self.assertEqual(calculate_area(5, 10), 50)
        self.assertEqual(calculate_area(0, 10), 0)

    def test_sort_numbers(self):
        self.assertEqual(sort_numbers([3, 1, 2]), [1, 2, 3])
        self.assertEqual(sort_numbers([]), [])

    def test_format_date(self):
        self.assertEqual(format_date("2024-03-22"), "22.03.2024")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertFalse(is_palindrome("hello"))

if __name__ == "__main__":
    unittest.main()
