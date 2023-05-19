import Figury_47
#enumeration - spis - wyliczanie

from enum import IntEnum
Menu_Figury = IntEnum('Menu_Figury', 'Prostokąt Kwadrat Trójkąt Trapez Koło Kończymy')



print("1. Wyznacz pole prostokąta ")
print("2. Wyznacz pole kwadratu ")
print("3. Wyznacz pole trójkąta ")
print("4. Wyznacz pole trapezu ")
print("5. Wyznacz pole koła ")
print("0. Kończymy ")
print()

wybor = int(input("Podaj swój wybór "))

if (wybor == Menu_Figury.Prostokąt):
    a = int(input("Podaj długość boku a "))
    b = int(input("Podaj długość boku b "))
    print("Pole prostokąta wynosi ",Figury_47.prostokat(a,b))
    print()
elif (wybor == Menu_Figury.Kwadrat):
    a = int(input("Podaj długość boku a "))
    print("Pole kwadratu wynosi ",Figury_47.kwadrat(a))
    print()
elif (wybor == Menu_Figury.Trójkąt):
    a = int(input("Podaj długość podstawy a "))
    h = int(input("Podaj długość wysokości h "))
    print("Pole trójkąta wynosi ", Figury_47.trojkat(a,h))
    print()
elif (wybor == Menu_Figury.Trapez):
    a = int(input("Podaj długość podstawy a "))
    b = int(input("Podaj długość podstawy b "))
    h = int(input("Podaj długość wysokości h "))
    print("Pole trapezu wynosi ", Figury_47.trapez(a,b,h))
    print()
elif (wybor == Menu_Figury.Koło):
    r = int(input("Podaj długość promienia r "))
    print("Pole koła wynosi ", Figury_47.kolo(r))
    print()
##elif wybor == "0":
##    print("Kończymy")
##    print()
##    break
else:
    print("Podałeś niewłaściwe dane... spróbuj ponownie")
    print()
