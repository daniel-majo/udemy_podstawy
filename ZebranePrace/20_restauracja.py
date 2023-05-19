'''Pracujesz dla restauracji, która chce nagrodzić klientów zamawiających
w dni robocze (poza weekendem) pizze lub duży napój.
Klienci spełniający warunki promocji dostaną kupon na darmowego burgera.
Na razie piszesz polecenie decydujące o spełnieniu warunków promocji.
Do dyspozycji masz zmienne:'''

isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = False

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print ("Gratuluję otrzymujesz kupon na darmowego burgera")
else:
    print ("Zachęcamy do zakupów w weekend... w calu otrzymania kuponu")
