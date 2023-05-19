from math import sqrt
print('Program liczący trójkąta prostokątnego')

a = int(input("Podaj długość boku a trójkąta: "))
b = int(input('Podaj długość boku b trójkąta: '))
c = sqrt(a**2+b**2)
print(f'Długość boku c wynosi {c}')