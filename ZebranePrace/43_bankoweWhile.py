'''Na konto została wpłacona kwota initialCapital w wysokości 20000.
Oprocentowanie na koncie to percent = 0.03.
Klient banku postanawia oszczędzać przez maxTimeYears = 10 lat.
Po każdym roku oszczędzania zarobiona kwota jest dodawana do oszczędności
i zarabia odsetki przez pozostały czas.

Zadeklaruj wymagane zmienne, a następnie stwórz pętlę,
która wyświetli informację o tym ile pieniędzy jest na koncie pod koniec roku,
kiedy odsetki się kapitalizują.
Dodaj na zakończenie informację o całkowitej kwocie zarobionej w banku.
'''

inicialCapital = 20000
percent = 0.03
maxTimeYears =10
oszczednosci = 0
i=0
capital=inicialCapital
while i < maxTimeYears:
    i+=1
    capital=((1+percent)*capital)
        
    oszczednosci = (capital-inicialCapital)
        
    print('Pod koniec ', i, 'roku Twoje oszczędności są w wysokości: ',int(capital))    
    
print ('Kwota całkowita zarobina to: ', int(oszczednosci))



##initialCapital = 20000
##percent = 0.03
##maxTimeYears = 10
##year=0
##capital=initialCapital
##while year<maxTimeYears:
##    year+=1
##    capital=round((1+percent)*capital,2) # x=round(wartosc, liczba) zaokrąglenie do dwóch miejsc po przecinku
##    print('after this year:', year,  'you will have:',capital)
##else:
##    print('the total revenue is', capital-initialCapital)
##print('-------------------------------------------------------')
