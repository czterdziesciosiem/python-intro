# my_awesome_lib/math_tools.py

def factorial(n: int) -> int:
    """Zwraca silnię liczby n."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def gcd(a: int, b: int) -> int:
    """Zwraca największy wspólny dzielnik (NWD) dwóch liczb."""
    while b:
        a, b = b, a % b
    return a
 
