# tests/test_text_processing.py
import unittest
from my_awesome_lib.text_processing import count_words

class TestTextProcessing(unittest.TestCase):
    def test_count_words(self):
        # Testy dla tekstów z różnymi znakami interpunkcyjnymi
        print(count_words("To jest test."))  # Oczekiwany wynik: 4
        self.assertEqual(count_words("To jest test."), 4)  # Oczekujemy 4 słowa, ponieważ kropka nie powinna wchodzić w liczenie
        
        print(count_words("Hello world!"))  # Oczekiwany wynik: 2
        self.assertEqual(count_words("Hello world!"), 2)  # 2 słowa z wykrzyknikiem
        
        print(count_words("Python 3.8"))  # Oczekiwany wynik: 2
        self.assertEqual(count_words("Python 3.8"), 2)  # 2 słowa, liczba i tekst
        
        print(count_words("test"))  # Oczekiwany wynik: 1
        self.assertEqual(count_words("test"), 1)  # Tylko jedno słowo
        
        print(count_words(""))  # Oczekiwany wynik: 0
        self.assertEqual(count_words(""), 0)  # Brak słów w pustym ciągu
        
        print(count_words("To, czy to jest test?"))  # Oczekiwany wynik: 5
        self.assertEqual(count_words("To, czy to jest test?"), 5)  # Test z przecinkami i pytajnikiem
        
        print(count_words("Python 3.8, test!"))  # Oczekiwany wynik: 3
        self.assertEqual(count_words("Python 3.8, test!"), 3)  # Test z cyframi i interpunkcją

if __name__ == "__main__":
    unittest.main()



