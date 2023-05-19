'''
Programowanie obiektowe

OOP - Object Oriented Programming
Programowanie zorientowane wokół obiektu

OBIEKT

OBIEKTY - to pojemniki do przechowywania zmiennych i funkcji tematycznie
        ze sobą powiązanych do dalszego łatwiejszego ponownego
        użycia

Klasy - formki (szablony) do tworzenia egzemplarzy obiektów

Atrybut - cecha opisująca obiekt
Metoda - funkcja, która operuje na obiekcie

Inicjacja klasy - instance z ang. egzemplarz to obiekt, który
                wyszedł z formy (klasy)
'''
class User:
    age = 18
    length = 150
    def print_age(first_name, age):
        print(f'{first_name} ma {age} lat.')

daniel = User()
ela = User()

age = 50

daniel.age = 43
daniel.length = 183

print(f'{daniel.length}, {ela.age}')

