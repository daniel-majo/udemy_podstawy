'''
__init__ - initialization - inicjalizacja - czyli ustawianie startowych
wartości dfla argumentów
w innych językach __init__ to konstruktor
'''
class User:
    age = '18'
    first_name = "Jan"
    height = '80'

    def __init__(self):
        print('Jestem inicjalizatorem, który wywołuje się zawsze podczas konstrukcji obiektu')
    def print_age(self, message):
        print(f'{self.first_name} ma {self.age} lat i {self.height} wzrostu. Wysłał/a wiadomość {message}')



user1 = User()
user2 = User()

user1.first_name = 'Daniel'
user2.first_name = 'Elżbieta'

user1.age = 44
# user2.age = 43

user1.height = 182
user2.height = 174

user1.print_age('jakiś dowoly tekst')
user2.print_age('jeszcze inny tekst')

