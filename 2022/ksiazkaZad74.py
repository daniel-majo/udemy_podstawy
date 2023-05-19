'''
Napisz program, który wypełnia dwuwymiarową tablicę 5 na 5 losowymi liczbami od 0 do 9, a następnie wyświetla w konsoli
tekst na podstawie wartości z tablicy. Kada z wartości reprezentuje znak specjalny nad numerem z klawiatury (1 - !,...),
które to znaki przechowujemy w tablicy:
c = ["!", "@","#", "$","%","^","&","*","(",")"]
'''
import random
t = [[],[],[],[],[]]
c = ["!", "@","#", "$","%","^","&","*","(",")"]
i = 0
while i < 5:
    j = 0
    while j < 5:
        t[i].append(random.randint(0,9))
        j += 1
    i += 1
i = 0
while i < 5:
    print(c[t[i][0]], c[t[i][1]], c[t[i][2]], c[t[i][3]], c[t[i][4]])
    i += 1
print(t)

