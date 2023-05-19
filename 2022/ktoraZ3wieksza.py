najwieksza = 0
a = int(input('Podaj wartość liczby '))
b = int(input('Podaj wartość liczby '))
c = int(input('Podaj wartość liczby '))
if a > b:
    if a > c:
        najwieksza = a
else:
    if b > c:
        najwieksza = b
    else:
        najwieksza = c
print('Najwieksza ' + str(najwieksza))