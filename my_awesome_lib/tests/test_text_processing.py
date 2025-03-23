# tests/test_text_processing.py
import unittest
from my_awesome_lib.text_processing import count_words

class TestTextProcessing(unittest.TestCase):
    def test_count_words(self):
        # Testy dla tekstów z różnymi znakami interpunkcyjnymi
        self.assertEqual(count_words("To jest test."), 4)  # Oczekujemy 4 słowa, ponieważ kropka nie powinna wchodzić w liczenie
        self.assertEqual(count_words("Hello world!"), 2)  # 2 słowa z wykrzyknikiem
        self.assertEqual(count_words("Python 3.8"), 2)  # 2 słowa, liczba i tekst
        self.assertEqual(count_words("test"), 1)  # Tylko jedno słowo
        self.assertEqual(count_words(""), 0)  # Brak słów w pustym ciągu
        self.assertEqual(count_words("To, czy to jest test?"), 5)  # Test z przecinkami i pytajnikiem, oczekiwane 5 słów
        self.assertEqual(count_words("Python 3.8, test!"), 3)  # Test z cyframi i interpunkcją, oczekiwane 3 słowa

if __name__ == "__main__":
    unittest.main()
