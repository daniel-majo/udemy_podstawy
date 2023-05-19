'''
Napisz program, który losuje dwie liczby i prosi użytkownika o podanie ich różnicy
'''
from random import randint

number1 = randint(1,100)
number2 = randint(1,100)
query = int(input(f'Podaj różnicę liczb {number1}-{number2} = '))
if query == (number1 - number2):
    print('Dobra odpowiedź')
else:
    print('Błąd')
