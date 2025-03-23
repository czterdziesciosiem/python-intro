# tests/test_text_processing.py
import unittest
from my_awesome_lib.text_processing import count_words

class TestTextProcessing(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("To jest test."), 4)
        self.assertEqual(count_words("Hello world!"), 2)
        self.assertEqual(count_words("Python 3.8"), 2)
        self.assertEqual(count_words("test"), 1)
        self.assertEqual(count_words(""), 0)

