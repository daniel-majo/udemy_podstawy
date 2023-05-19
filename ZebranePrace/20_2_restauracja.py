'''Pracujesz dla restauracji, która chce nagrodzić klientów zamawiających
w dni robocze (poza weekendem) pizze lub duży napój.
Klienci spełniający warunki promocji dostaną kupon na darmowego burgera.
Na razie piszesz polecenie decydujące o spełnieniu warunków promocji.
Do dyspozycji masz zmienne:'''

isPizzaOrdered = True
isBigDrinkOrdered = True
isWeekend = False

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print ("Gratuluję otrzymujesz kupon na darmowego Burgera")
elif isWeekend:
    print ("Zachęcamy do zakupów w tygodniu... w calu otrzymania kuponu")
else:
    print ("Zachęcamy do zakupienia Pizzy lub dużego napoju... w calu otrzymania kuponu")
print ("--------------")         
