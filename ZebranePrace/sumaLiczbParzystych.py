'''
Napisz program, który doda kolejne 3 parzyste liczby podane przez użytkownika
'''

suma = 0
i = 3

while i > 0:
    x = int(input("Podaj liczbę: "))
    if (x%2 == 0 and x>0):
        suma = suma + x
        i-=1
    else:
        print("Podaj liczbę dodatnią i parzystą")
print("Suma liczb to:", suma)
