# My Awesome Lib

My Awesome Lib to biblioteka Pythona, która oferuje zestaw narzędzi do manipulacji danymi, obliczeń matematycznych i przetwarzania tekstu. Została zaprojektowana, aby ułatwić codzienne zadania, takie jak konwersja temperatur, obliczenia matematyczne oraz analiza tekstu.

## Funkcje

- **Konwersja temperatur**: Konwertowanie temperatur pomiędzy Celsjuszem a Fahrenheitem.
- **Narzędzia matematyczne**: Wykonywanie popularnych operacji matematycznych, takich jak obliczanie silni czy sprawdzanie, czy liczba jest liczbą pierwszą.
- **Przetwarzanie tekstu**: Analiza tekstu, w tym liczenie słów oraz znajdowanie najczęściej występującego słowa.

## Instalacja

Aby zainstalować **My Awesome Lib**, użyj `pip`. Możesz to zrobić w następujący sposób:

```bash
pip install my_awesome_lib

Jeśli pracujesz lokalnie nad biblioteką i chcesz zainstalować ją w trybie edytowalnym (aby móc modyfikować kod bez potrzeby ponownej instalacji), użyj:
pip install -e .

## Użycie

Data Utils
Moduł data_utils oferuje funkcje do konwersji danych, takie jak konwersja temperatur. Oto jak można go używać:

from my_awesome_lib.data_utils import convert_to_celsius, convert_to_fahrenheit

# Konwertowanie 100 stopni Fahrenheita na Celsjusza
print(convert_to_celsius(100))  # Wynik: 37.77777777777778

# Konwertowanie 37.777 stopni Celsjusza na Fahrenheita
print(convert_to_fahrenheit(37.777))  # Wynik: 100.0


Math Tools
Moduł math_tools oferuje funkcje matematyczne, takie jak obliczanie silni liczby czy sprawdzanie, czy liczba jest liczbą pierwszą:

from my_awesome_lib.math_tools import factorial, is_prime

# Obliczanie silni liczby 5
print(factorial(5))  # Wynik: 120

# Sprawdzanie, czy liczba jest liczbą pierwszą
print(is_prime(7))  # Wynik: True


Text Processing
Moduł text_processing zawiera funkcje do analizy i przetwarzania tekstu, takie jak liczenie słów czy znajdowanie najczęściej występującego słowa:

from my_awesome_lib.text_processing import count_words, most_frequent_word

# Liczenie słów w zdaniu
sentence = "To jest testowe zdanie."
print(count_words(sentence))  # Wynik: 5

# Znalezienie najczęściej występującego słowa
text = "hello hello world"
print(most_frequent_word(text))  # Wynik: hello


Licencja
Ten projekt jest licencjonowany na zasadach licencji MIT

Wersja
Aktualna wersja: 1.0.0

Autor
Tomasz Łagowski
Kontakt: tomaszlagowski@spoko.pl
