maks = 0

for i in range(5):
    a = int(input('Podaj liczbę:'))
    if a > maks:
        maks = a
print("MAX:" + str(maks))

input('\nNaciśnij ENTER aby wyjść')
