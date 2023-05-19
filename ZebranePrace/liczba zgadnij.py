liczba=19
pytanie=int(input("Podaj liczbę jaką mam na mysli"))
if pytanie==int(liczba):
    print ('BRAWO! Własnie tą liczbe miałem na mysli')
elif pytanie>liczba:
    print ('Moja liczba',liczba,' jest mniejsza od Twojej', pytanie)
else:
    pytanie<liczba
    print ('Moja liczba',liczba,' jest większa od Twojej', pytanie)
print ('KONIEC')

