import random
uzytkownik = input("Podaj swoją propozycję (papier, kamien lub nozyczki) ")
losowanie = random.randint(1,3);

##papier = 1
##kamien = 2
##nozyczki = 3


if losowanie == 1:
    print ("PC - papier")
    if uzytkownik == "papier":
        print ("Remis")
    if uzytkownik == "kamien":
        print ("Przegrałes")
    if uzytkownik == "nozyczki":
        print ("Wygrałes")
if losowanie == 2:
    print ("PC - kamien")
    if