# typy zagnieżdżone

imie = 'Daniel'
wiek = 42
plec = 'mężczyzna'

imie = 'Adam'
wiek = 38
plec = 'mężczyzna'

imie = 'Elżbieta'
wiek = 28
plec = 'kobieta'

osoba1 = ('Daniel',42,'mężczyzna')
osoba2 = ('Adam',38,'mężczyzna')
osoba3 = ('Elżbieta',42,'kobieta')

listaGosci = [
                ('Daniello',42,'mężczyzna'),
                ('Adam',38,'mężczyzna'),
                ('Elżbieta',42,'kobieta')
    ]

listaGosci2 = [
                ('Daniello',22,'mężczyzna'),
                ('Adamina',21,'kobieta'),
                ('Edward',24,'mężczyzna')
    ]



listaGosci.append(('Zumburak',12,'mężczyzna'))

    
#- dodajemy do krotki nie wiedząc na które miejsce zostanie dopisane 

''' Dodawanie do listy - ważna jest kolejność... dodajemy na koniec append, natomiast w set czyli słowniku nie ma
znaczenia, dodajemy nie wiedząc na które miejsce dlatego add
#listaGosci.append['Zumburak',12,'mężczyzna'] - dodajemy na sam koniec 

# listaGosci[0][1]=22 - podmianka danych w liście listaGosci'''

'''listaGosci3 = listaGosci | listaGosci2  #suma | , & część wspólna

for imie, wiek, plec in listaGosci3:
    print("Imię", imie)
    print("Wiek", wiek)
    print("Płeć", plec)
    print("\n")'''


