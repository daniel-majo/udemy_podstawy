'''
Stwórz menu, z którego użytkownik, może wybrać opcje, aby policzyć powierzchnie
figur:

1) prostokąta
2) kwadratu
3) trójkąta
4) trapezu
5) koła

Pamiętaj, by skorzystać z funkcji.
'''

def prostokat(a,b):
    return a*b

def kwadrat(a):
    return a*a

def trojkat(a,h):
    return a*h/2

def trapez(a,b,h):
    return (a+b)*h/2

def kolo(r):
    return 3.14*r*2

'''
while(True):
    print("1. Wyznacz pole prostokąta ")
    print("2. Wyznacz pole kwadratu ")
    print("3. Wyznacz pole trójkąta ")
    print("4. Wyznacz pole trapezu ")
    print("5. Wyznacz pole koła ")
    print("0. Kończymy ")
    print()

    wybor = input("Podaj swój wybór ")

    if wybor == "1":
        a = int(input("Podaj długość boku a "))
        b = int(input("Podaj długość boku b "))
        print("Pole prostokąta wynosi ",prostokat(a,b))
        print()
    elif wybor == "2":
        a = int(input("Podaj długość boku a "))
        print("Pole kwadratu wynosi ",kwadrat(a))
        print()
    elif wybor == "3":
        a = int(input("Podaj długość podstawy a "))
        h = int(input("Podaj długość wysokości h "))
        print("Pole trójkąta wynosi ", trojkat(a,h))
        print()
    elif wybor == "4":
        a = int(input("Podaj długość podstawy a "))
        b = int(input("Podaj długość podstawy b "))
        h = int(input("Podaj długość wysokości h "))
        print("Pole trapezu wynosi ", trapez(a,b,h))
        print()
    elif wybor == "5":
        r = int(input("Podaj długość promienia r "))
        print("Pole koła wynosi ", kolo(r))
        print()
    elif wybor == "0":
        print("Kończymy")
        print()
        break
    else:
        print("Podałeś niewłaściwe dane... spróbuj ponownie")
        print()
'''        


    
    
