from enum import IntEnum
dniTygodnia = IntEnum('dniTygodnia', 'Poniedziałek Wtorek Środa Czwartek Piątek Sobota Niedziela')

print('Program wskazujący dzień tygodnia na podstawie podanej liczby ')
print()
while(True):
    zapytanie = int(input("Podaj wartość od 1 do 7, ja podam jaki to jest dzień tygodnia "))

    if (zapytanie ==dniTygodnia.Poniedziałek):
        print('Poniedziałek')
    elif (zapytanie ==dniTygodnia.Wtorek):
        print('Wtorek')
    elif (zapytanie ==dniTygodnia.Środa):
        print('Środa')
    elif (zapytanie ==dniTygodnia.Czwartek):
        print('Czwartek')
    elif (zapytanie ==dniTygodnia.Piątek):
        print('Piątek')
    elif (zapytanie ==dniTygodnia.Sobota):
        print('Sobota')
    elif (zapytanie ==dniTygodnia.Niedziela):
        print('Niedziela')
    else:
        print("Podaj wartość od 1 do 7 ")
