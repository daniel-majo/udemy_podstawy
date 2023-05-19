'''
Przygotuj funkcję, która odbierze od użytkownika liczbę, a następnie zwróci w odpowiedzi wynik True lub False w zależności od tego, 
czy podana liczba jest pierwsza
'''
#zaokrąglenie liczby w górę
from math import ceil, sqrt

def is_prime(number: int) -> bool:
    for n in range(2, ceil(sqrt(number)) + 1):
        if number % n == 0:
            return False

    return True

print(is_prime(9))
print(is_prime(7))