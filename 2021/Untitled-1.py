'''
Zadanie 1 część 3 z PasjaInformactyki
Przygotuj funkcję, która odbierze od użytkownika liczbę, a następnie zwróci słownik wyglądający w ten sposób
{
    "liczba":30,
    "kwadrat":900,
    "sześcian":27000
}

'''
from math import pow
value = int(input('Podaj liczbę: '))
power = pow(value, 2)
power3 = pow(value,3)
print(f'{value}, {power}, {power3}')