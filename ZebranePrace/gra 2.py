print('Witamy w Milionerach')
print('Przed tobą 10 pytań')
print('Za każde 1000 zł')
print('Dobrze. Więc zacznijmy!')
wynik = 0
numpyt = 0

# Pytanie 1

numpyt = numpyt + 1
podp = 1
print('Pytanie',numpyt)
print('Od czgo nazywa się program Python?')
odp = input('Od 1. Latającego Cyrku Monte Pythona, 2. Pytona czy 3. To nazwa własna')
if podp == int(odp):
    wynik = wynik + 1000
    numpyt = numpyt + 1
    print('Poprawna odpowiedź! Następne pytanie.')
    print(wynik)

#elif podp != int(podp):
    #print('Zła odpowiedz! Wygrana', wynik ,'zł')

else:
    print('Zła odpowiedz! Wygrana', wynik ,'zł')


# Pytanie 2

podp = 3
print('Pytanie',numpyt)
print('Czy pielęgnica Papuzia to:')
odp = input('1. Ptak, 2.Ssak czy 3.Ryba?')
if podp == int(odp):
    wynik = wynik + 1000
    numpyt = numpyt + 1
    print('Poprawna odpowiedź! Następne pytanie.')
    print(wynik)
else:
    print('Zła odpowiedz! Wygrana', wynik ,'zł')

# Pytanie 3

podp = 2
print('Pytanie',numpyt)
print('Mazurka Dąbrowskiego stworzył:')
odp = input('1. Marszałek Dąbrowski, 2. Józef Wybicki czy 3.Autor Nieznany?')
if podp == int(odp):
    wynik = wynik + 1000
    numpyt = numpyt + 1
    print('Poprawna odpowiedź! Następne pytanie.')
    print(wynik)
else:
    print('Zła odpowiedz! Wygrana', wynik ,'zł')

# Pytanie 4

podp = 3
print('Pytanie',numpyt)
print('Pierwsza stolica Polski to:')
odp = input('1.Kraków, 2.Opole czy 3.Gniezno?')
if podp == int(odp):
    wynik = wynik + 1000
    numpyt = numpyt + 1
    print('Poprawna odpowiedź! Następne pytanie.')
    print(wynik)
else:
    print('Zła odpowiedz! Wygrana', wynik ,'zł')

# Pytanie 5

podp = 2
print('Pytanie',numpyt)
print('Polska wstąpiła do Uni Europejskiej w:')
odp = input('1.1994, 2.2004 czy 3.2014?')
if podp == int(odp):
    wynik = wynik + 1000
    numpyt = numpyt + 1
    print('Poprawna odpowiedź! Następne pytanie.')
    print(wynik)
else:
    print('Zła odpowiedz! Wygrana', wynik ,'zł')


# Pytanie 6

podp = 3
print('Pytanie',numpyt)
print('Fotosynteza to termin oznaczający:')
odp = input('1.syntezę światła,, 2.album przyrodniczy czy 3.proces wytwarzania pożywienia?')
if podp == int(odp):
    wynik = wynik + 1000
    numpyt = numpyt + 1
    print('Poprawna odpowiedź! Następne pytanie.')
    print(wynik)
else:
    print('Zła odpowiedz! Wygrana', wynik ,'zł')
