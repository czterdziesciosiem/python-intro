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

    # Używamy wyrażenia regularnego, które zlicza słowa
    words = re.findall(r'\b\w+\b', text)

    return len(words)







 
