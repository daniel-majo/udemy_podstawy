##a = int(input("Podaj liczbę: "))
##if a%2==0:
##    print("Liczba parzysta")
##else:
##    print("Liczba nieparzysta")
'''
liczba = int(input("Podaj liczbę do rozłożenia: "))
while liczba>0:
    print(liczba%10)
    liczba = liczba//10
'''

##wyraz = str(input("Podaj swój wyraz: "))

##for slowo in wyraz:
##        print("Nazwa", wyraz[0])
##        print("Litera",slowo)
##for i in range(len(wyraz)-1):
##    print(wyraz[i:i+2])

'''
liczba maksimum na liście
'''

##liczby = [2, 45, 64, 1, 0,18,22]
##maks = liczby[0]
##
##for i in liczby:
##    if i > maks:
##        maks = i
##print(maks)
##
##maks = liczby[0]
##poz = 0
##
##for i in range(len(liczby)):
##    if liczby[i] > maks:
##        maks = liczby[i]
##        poz = i
##print("Pozycja", poz+1, "liczby maksymalnej", maks)

'''
Tworzenie listy
'''
lista =[]
n = int(input("Ile liczb chcesz podać: "))

for i in range(n):
    x = int(input("Podaj liczbę: "))
    lista.append(x)
print(lista)
    
