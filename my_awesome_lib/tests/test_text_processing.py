# tests/test_text_processing.py
import unittest
from my_awesome_lib.text_processing import count_words

class TestTextProcessing(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("To jest test."), 4)  # Test dla tekstu z kropką
        self.assertEqual(count_words("Hello world!"), 2)  # Test dla tekstu z wykrzyknikiem
        self.assertEqual(count_words("Python 3.8"), 2)  # Test dla tekstu z liczbami
        self.assertEqual(count_words("test"), 1)  # Test dla pojedynczego słowa
        self.assertEqual(count_words(""), 0)  # Test dla pustego ciągu znaków

