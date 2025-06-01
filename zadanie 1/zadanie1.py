import math

# Tworzenie dwóch list
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Łączenie list za pomocą zip()
zipped = list(zip(list1, list2))
print("Połączone listy:", zipped)

# Użycie funkcji z modułu math
print("Pierwiastek z 16:", math.sqrt(16))

# Obsługa wyjątku
try:
    number = int(input("Podaj liczbę: "))
    result = 10 / number
    print("Wynik:", result)
except ZeroDivisionError:
    print("Błąd: Dzielenie przez zero!")
except ValueError:
    print("Błąd: Nieprawidłowa wartość!")

# Linki do dokumentacji:
# zip(): https://docs.python.org/3/library/functions.html#zip
# math.sqrt(): https://docs.python.org/3/library/math.html
# ZeroDivisionError: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError

 
