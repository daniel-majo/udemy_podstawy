''' Szukanie liczby największej w liczbie całkowitej
'''
##liczba = int(input("Podaj liczbę całkowitą: "))
##
##maks = 0
##
##while liczba > 0:
##    r = liczba%10
##    if r > maks:
##        maks = r
##    liczba = liczba //10
##print("Liczba maksymalna to: ", maks)
'''
szukamu litery w wyrazie
'''
##napis = str(input("Podaj wyraz: "))
##litera = str(input("Podaj literę, której szukamy: "))
##
##i = 0
##
##while i < len(napis) and napis[i] !=litera:
##    i = i + 1
##
##if i == len(napis):
##    print("Podanej literki nie ma w napisie")
##else:
##    print("Podana litera jest na pozycji",i + 1)
'''
Komputer odgaduje liczbę
'''
##a = 0
##b = 100
##print("Pomyśl liczbę z ptzedziału od <0,100>")
##input("Naciśnij Enter, aby przejść dalej")

##while a < b:
##    c = (a+b)//2 #dzielimy przedział całkowity na dwa
##    x = input("Czy pomyślana liczba jest większa niż "+ str(c)+ " t/n? ")
##    if x.lower() == 't' or x =='T':
##        a = c + 1
##    else:
##        b = c
##print("Pomyślana liczba to: ",a)

'''
szukanie w biorze uporządkowanym
'''
##from random import randint
##lista = [randint(4*x,4*(x+1)) for x in range(20)]
##print(lista)
##
##szukana = int(input("Szukana liczba "))
##a = 0; b = len(lista) - 1
##
##while a < b:
##    print(a,b)
##    c = (a+b)//2
##    if szukana > lista[c]:
##        a = c + 1
##    else:
##        b = c
##if lista[a] == szukana:
##    print(szukana, " jest na liście")
##else:
##    print(szukana, " nie występuje na liście")
'''
losowanie kostką
'''
##for i in range(10):
##    print("Wylosowano ", randint(1,6))
##    print("liczba 6 wylosowana ", , "razy")

##tekst = "Daniel Majewski"
##print(len(tekst),"znaków w tekście")
##for znak in tekst:
##    if znak !=' ':
##        print(znak)

i=0
wynik = 0
for i in range(0,4):
    x = int(input("Podaj liczbę"))
    wynik += x
    print(wynik)