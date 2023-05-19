lista_liczb = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
lista_slow = [ 'poniedziałek' , 'wtorek' , 'środa' , 'czwartek', 'piątek' , 'sobota' , 'niedziela' ]

# dla każdej liczby w liscie lista_liczb, dodaje i wyswietla tresc 'Kolejna liczba to: liczba'/traktując jako tekst/
for liczba in lista_liczb:
	print ('Kolejna liczba to ' + str(liczba) )

for slowo in lista_slow:
	print ('Kolejny dzien tygodnia to ' + slowo )

# .count() wyszukuje tylko tresci o wartosci 2
lista_liczb.count(2)
new_list=lista_liczb.count(2)
print (new_list)

# [] wyswietla z operatora index 0, czyli tylko 'poniedziałek'
lista_slow[0]
print (lista_slow[0])

# dodawanie dwoch list i ich wyswietlanie
nowa_lista = lista_liczb + lista_slow
print (nowa_lista)

# len() pobiera długosc, a więc zlicza ilosc elementow
ilosc_liczb=len(lista_liczb)
print (ilosc_liczb)
