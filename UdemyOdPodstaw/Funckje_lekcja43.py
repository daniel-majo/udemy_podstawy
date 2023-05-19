'''
Funkcja - to blok kodu do któreo można się
w każdej chwili odwołać aby otrzymać przez nas wynik

def nazwa_funkcji():
    instrukcja1
    instrukcja2

nazwa_funkcji()

'''

print("Witam Cię, Arku na programowaniu z Pythona")
print("Witam Cię, Olu na programowaniu z Pythona")
print("Witam Cię, Bartku na programowaniu z Pythona")
print("wynik wersji 1")
print()

def wiadomosc_powitalna():#użycie prostej funkcji 

    print("Witam Cię, Arku na programowaniu z Pythona")
    print("Witam Cię, Olu na programowaniu z Pythona")
    print("Witam Cię, Bartku na programowaniu z Pythona")

wiadomosc_powitalna()
print("wynik wersji 2")
print()



def wiadomosc_powitalna(imie):#użycie funkcji z argumentem imie

    print("Witam Cię,", imie," na programowaniu z Pythona")
    
wiadomosc_powitalna("Arku")
wiadomosc_powitalna("Olu")
wiadomosc_powitalna("Bartku")
print("wynik wersji 3")
print()

def wiadomosc_powitalna(imie): #użycie funkcji z argumentem przez pętlę for

    print("Witam Cię,", imie," na programowaniu z Pythona")

imiona =["Arku", "Olu", "Bartku"]

for imie in imiona:
    wiadomosc_powitalna(imie)

print("wynik wersji 4")
