# tests/test_text_processing.py
import unittest
from my_awesome_lib.text_processing import count_words, remove_special_chars

class TestTextProcessing(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual(count_words("To jest test."), 4)
        self.assertEqual(count_words("Python!"), 1)

    def test_remove_special_chars(self):
        self.assertEqual(remove_special_chars("Python@#123!"), "Python123")
        self.assertEqual(remove_special_chars("Hello, World!"), "Hello World")
        
if __name__ == '__main__':
    unittest.main()
 
