'''
Zadanie 1 część 3 z PasjaInformactyki
Przygotuj funkcję, która odbierze od użytkownika liczbę, a następnie zwróci słownik wyglądający w ten sposób
{
    "liczba":30,
    "kwadrat":900,
    "sześcian":27000
}

'''

def get_double_cube(number: int) -> dict:
    double = number ** 2
    cube = number ** 3
    return {
        "liczba":number,
        "kwadrat":double,
        "sześcian":cube
    }

print(get_double_cube(4))
