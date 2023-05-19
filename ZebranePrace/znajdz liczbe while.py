liczba=19
running=True
while running:
    pytanie=int(input("Podaj liczbę jaką mam na mysli"))
    if pytanie==int(liczba):
        print ('BRAWO! Własnie tą liczbe miałem na mysli')
        print ('Moja liczba to\n',liczba)
        running=False
    elif pytanie>liczba:
        print ('Moja liczba jest mniejsza od Twojej')
    else:
        pytanie<liczba
        print ('Moja liczbajest większa od Twojej')
print ('KONIEC')