maks = 0
grubas = int(input("Podaj ilość liczb w zbiorze"))
for i in range(grubas):
    a = int(input('Podaj liczbę:'))
    if a > maks:
        maks = a
print("Największa liczba w tym zboirze to::" + str(maks))

input('\nNaciśnij ENTER aby wyjść')
