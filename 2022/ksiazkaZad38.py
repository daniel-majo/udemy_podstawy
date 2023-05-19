'''
Napisz program, który losową liczbe razy - od 1 do 15 - powtarza napis wpisany do konsoli przez użytkownika
'''
from random import randint

string = str(input('Podaj tekst do powielenia '))
repetition = randint(1,15)
print(f'{repetition * string}')