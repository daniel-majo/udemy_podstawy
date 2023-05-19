'''
Niech a będzie zmienną równą 3. Niech b będzie zmienną trzy razy większa niż a.
Napisz program, który losuje liczbę z przedziału od a do b
'''
from random import randint
a = 3
b = 3*a

value = randint(a, b)
print(value)