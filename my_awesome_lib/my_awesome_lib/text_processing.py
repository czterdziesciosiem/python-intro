# my_awesome_lib/text_processing.py

import re

def count_words(text):
    """
    Zlicza liczbę słów w tekście, traktując słowo jako ciąg znaków oddzielony spacjami lub znakami interpunkcyjnymi.

    :param text: Tekst, w którym będą liczone słowa.
    :return: Liczba słów w tekście.
    """
    # Używamy wyrażenia regularnego, aby znaleźć wszystkie słowa (ciągi literowe, liczbowe) oddzielone spacjami lub interpunkcją
    words = re.findall(r'\b\w+\b', text)
    return len(words)


 
