# drukowanie na ekranie tekstu
print ('Witaj w Pythonie!')
print ('''Witaj w Pythonie ponownie!''')

# drukowanie wartosci liczbowych z zakresu (1,10)
for liczba in range(1,10):
    print (liczba)

# definiowanie funkcji i odwoływanie się do niej
def mojaFunkcja(liczba):
	return liczba*2
x=2
print (mojaFunkcja(x))

# operator indeksowania
a='Witaj w Pythonie'
print (a[0])
print (a[0:5])

# łączene tekstu z wartosciami liczbowymi
a = 'Witaj w swieciePythona'
b = ' w 2019 roku. Szczesliwy numerek to: '
c = 13
#print (a+b+c)
print (a+b+str(c))
print (a+b+repr(c))

''' operacje matematyczne
można dodatkowo funkcję print (int(a/b))'''
a = 5
b = 2
print (a+b)
print (a*b)
print (a/b)
print (a%b)


# drukowanie rożnych łączonych tresci
a=2
b=5
wynik = a/b
poczatek= 'Wynik dzielenia liczb 2 i 5 wynosi:'
koniec = 'co bylo oczekiwane'
print (poczatek,wynik,koniec)

# listy
lista = ['element1 ', 'element2 ', 'element3 ', 15.5]
print (lista)
lista[3] = 'koziolek'
print (lista)
print (len(lista))
lista.append("Uczniowie")
print (lista)

# tuple

tuple = ['Poniedzialek', 15, 'Wtorek', 'Sroda', 'Czwartek', 'Piatek']
print (tuple)


