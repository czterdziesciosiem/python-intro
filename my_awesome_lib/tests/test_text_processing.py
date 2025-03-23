# tests/test_text_processing.py
import unittest
from my_awesome_lib.text_processing import count_words

class TestTextProcessing(unittest.TestCase):
    def test_count_words(self):
        # Wydrukowanie wyników przed porównaniem
        result = count_words("To jest test.")
        print("Wynik: ", result)
        self.assertEqual(result, 4)  # Oczekujemy 4 słowa, ponieważ kropka nie powinna wchodzić w liczenie
        
        result = count_words("Hello world!")
        print("Wynik: ", result)
        self.assertEqual(result, 2)  # 2 słowa z wykrzyknikiem
        
        result = count_words("Python 3.8")
        print("Wynik: ", result)
        self.assertEqual(result, 2)  # 2 słowa, liczba i tekst
        
        result = count_words("test")
        print("Wynik: ", result)
        self.assertEqual(result, 1)  # Tylko jedno słowo
        
        result = count_words("")
        print("Wynik: ", result)
        self.assertEqual(result, 0)  # Brak słów w pustym ciągu
        
        result = count_words("To, czy to jest test?")
        print("Wynik: ", result)
        self.assertEqual(result, 5)  # Test z przecinkami i pytajnikiem
        
        result = count_words("Python 3.8, test!")
        print("Wynik: ", result)
        self.assertEqual(result, 3)  # Test z cyframi i interpunkcją

if __name__ == "__main__":
    unittest.main()


