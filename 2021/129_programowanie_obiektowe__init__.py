'''
__init__ - initialization - inicjalizacja - czyli ustawienie
startowych wartości dla atrybutów

w innych językach __init__ to konstruktor
'''
class User: #klasy z Dużej litery
    def __init__(self, age, first_name):
        print('Jestem inicjalizatorem, który wowołuje się zawsze podczas konstrukcji obiektu')
        self.age = age
        self.first_name = first_name

    def print_age(self, message):
        print(f'{self.first_name} ma {self.age} lat. Wysłał/a wiadomość {message}')

user1 = User(44, 'Daniel')
user2 = User(43, 'Elżbieta')

user1.print_age('jakiś dowoly tekst')
user2.print_age('jeszcze inny tekst')