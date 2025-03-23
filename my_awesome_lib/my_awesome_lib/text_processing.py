# my_awesome_lib/text_processing.py

import re

def count_words(text):
    """
    Zlicza liczbę słów w tekście, traktując słowo jako ciąg znaków alfanumerycznych oddzielony spacjami lub znakami interpunkcyjnymi.
    :param text: Tekst, w którym będą liczone słowa.
    :return: Liczba słów w tekście.
    """
    # Usuwamy nadmiarowe białe znaki na początku i końcu
    text = text.strip()

    # Usuwamy interpunkcję z końca tekstu (ale pozostawiamy spacje pomiędzy słowami)
    text = re.sub(r'[^\w\s]', '', text)  # Usuwamy wszystko, co nie jest literą, cyfrą lub spacją

    # Zliczamy słowa
    words = re.findall(r'\b\w+\b', text)

    return len(words)

# Przykłady testowe
print(count_words("To jest test."))  # Powinno wypisać 4
print(count_words("Hello world!"))  # Powinno wypisać 2
print(count_words("Python 3.8"))  # Powinno wypisać 2
print(count_words("test"))  # Powinno wypisać 1
print(count_words(""))  # Powinno wypisać 0
print(count_words("To, czy to jest test?"))  # Powinno wypisać 5
print(count_words("Python 3.8, test!"))  # Powinno wypisać 3

















 
