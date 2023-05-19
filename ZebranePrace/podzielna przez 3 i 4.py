ile=int(input("Podaj ilosc powtorzeń"))
if ile<=0:
    print ('Koniec, nie wpisałes żadnej wartosci dodatniej')
for liczba in range(0,ile):
        a=int(input('Podaj liczbę'))
        if a%3==0:
            print ('Liczba podzielna przez 3')
        if a%4==0:
            print ('Liczba podzielna przez 4')
        if a%3==0 and a%4==0:
            print ('Hurra! Liczba podzielna przez 3 i przez 4')
        if a%3!=0 and a%4!=0:
            print ('*')
else:
    print ('Koniec skryptu')
