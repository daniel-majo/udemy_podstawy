licznik = 10
suma = 0
liczba = 0

while licznik !=0:
    liczba = int(input("Podaj liczbę "))
    if liczba > 5:
        suma +=liczba
        licznik -=1 
    else:
        print("Podaj liczbę większą od 5")
print("Suma liczb to :", suma)
