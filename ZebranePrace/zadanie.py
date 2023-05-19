

'''quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'
Wyświetl tekst napisany tylko wielkimi literami
Wyświetl tekst zapisany tylko małymi literami
Sprawdź czy tekst kończy się słowem 'street'
Sprawdź czy tekst jest zapisany wielkimi literami
Sprawdź, czy tekst skonwertowany do wielkich liter jest zapisany wielkimi literami (Zastosuj złożenie funkcji)
Poszukaj na której pozycji (licząc od zera) znajduje się w tekście słowo 'one'
Zamień w tekście słowo 'one' na '1'
Zamień w tekście słowo 'one' na '1' a słowo 'both' na 2
Rozdziel napis na mniejsze napisy ze względu na znak rozdzielający jakim jest spacja



quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'
#print (quote.upper())
#print (quote.lower())
#print(quote.endswith('street'))
#print (quote.startswith('A'))
#print (quote.isupper())
#print (quote.upper().isupper())
#print (quote.find('one',0))
#print(quote.split(' '))
#print (quote.count('m'))     #ilość występowania znaków 'm'
#print(quote.isdigit())      # liczba 
#print(quote.isdecimal())    # 
#print(quote.isalpha())
#print(quote.isalnum())

#join_tekst = ' '
#print (join_tekst.join(['A','good','programmer','is','...','street']))        #łączenie elementów listy w jeden string

#text = 'Imię i nazwisko\nDaniel Majewski'
#print (text)

#Zmienna_tekst = 'Powielona treść'
#print ('Zmienna_tekst ' * 10)



# sprawdzanie pozycji w tekście

	
# Zwracanie pozycji tekstu w innym tekscie
#x = "Mieszkam w Polsce i uczę się programowania"
#print(x.index("k"))
#print(x.index("programowania"))


# rozbudowana funkcja print()
    #   %s, by wstawić wartość tekstową,
    #   %d, by wstawić liczbę całkowitą int,
    #   %f, by wstawić liczbę float.

# po nazwie zmiennej wprowadzamy % i nawias. W nawiasie wartość lub nazwy zmiennych

# imię
imie = input("Jak masz na imię? ")
print ("Witam Cię", imie)


# 1. wstawienie liczby całkowitej w tekście: %d
tekst1="Ja mam %d lat."

x = 15

print (tekst1 %x)

# 2. używamy więcej niż jedną zmienną
tekst2 = "Ja  mam %d lat i mieszkam we %s."

x = 15
y = 'Włocławku'

print (tekst2 %(x,y))

# 3. wstawiamy więcej niż jedną zmienną o tym samym typie danych

tekst3 = "%s jest z %s. Ma %d lat. Z testu z Pythona w klasie %d w %d roku zdobył %.1f punktów"
klasa = 8
wiek = 15
pkt = 87.5
rok = 2020
miasto = "Włocławka"

print (tekst3 %(imie,miasto,wiek,klasa,rok, pkt))


# 4. wstawiamy więcej niż jedną zmienną o tym samym typie danych z rezerwacją znaków

tekst4 = "%s jest z %10s. Ma %d lat. Z testu z Pythona w klasie %d w %d roku zdobył %5.1f punktów"
klasa = 8
wiek = 15
pkt = 87.5
rok = 2020
miasto = "Włocławka"

print (tekst4 %(imie,miasto,wiek,klasa,rok, pkt))



# nowsze notacje

wiadomosc1 = 'Przetwarzanie pliku {0:s}'        #wykorzystanie tylko jednego parametru typu tekst
print (wiadomosc1.format('plik1.txt'))

wiadomosc2 = 'Plik {0:s} ma rozmiar {1:d} KB'   #wykorzystanie parametru tekstu i liczby
print (wiadomosc2.format('plik1.txt',200))

wiadomosc3 = 'Plik {1:s} ma rozmiar {0:d} KB'   #zamiana miejscami parametrów
print (wiadomosc3.format(200, 'plik1.txt'))

wiadomosc4 = 'Plik {1:20s} ma rozmiar {0:10d} KB'   #rezerwacja ilości znaków
print (wiadomosc4.format(200, 'plik1.txt'))

#Polecenie

1. Utwórz zmienną cennik i wpisz do niej tekst pozwalający na wyświetlenie w 30 znakach pewnego napisu, nastepnie słowa cena, oraz na 5 znakach pewnej liczby

Lody                    cena          4
Wycieczka do Wenecji    cena        256
Pizza Hawajska          cena         25

2. Korzystając  ze zmiennej cennik i polecenia print, zamieniaj odpowiednie znaczniki na podane wyżej wartości, tak aby w efekcie został wyświetlony cennik usług.


#starsza notacja
text = "%-30s cena %5d"               # - wyrównanie do lewej
print(text%("Lody", 4))
print(text%("Wycieczka do Wenecji", 256))
print(text%("Pizza Hawajska", 25))

# nowsza notacja
text = "{0:30s} cena {1:5d}"               # - wyrównanie do lewej
print(text.format("Lody", 4))
print(text.format("Wycieczka do Wenecji", 256))
print(text.format("Pizza Hawajska", 25))

'''

#print ("A"<"a")
#print (input("Podaj pierwszą liczbę ") != input("Podaj drugą liczbę "))

#print (int(input("Podaj L1 "))+int(input("Podaj L2 ")) < 100)
'''
password = input ("Podaj hasło: ")

if (input("Podaj hasło: ")==("sp5")):
    print ("Komnata została otwarta")
else:
    print ("Hasło nieprawidłowe")


if int(input("Podaj wartość pola kwadratu dla boku 5: ")) == 25:
    print ("BRAWO!")
else:
    print ("Próbuj dalej...")
'''

#print ("suma liczb: " ,(int(input("podaj liczbę"))+int(input("podaj liczbę"))))


# sygnalizacja świetlna


swiatlo = input("Jakie jest światło? (czerwone, zielone, pomaranczowe) ")


if  swiatlo == "czerwone":
    print ("Stój!!")
    input("Wciśnij Enter aby wyjść")
elif swiatlo == "pomaranczowe":
    print ("Przygotuj się!")
    input("Wciśnij Enter aby wyjść")
elif swiatlo == "zielone":
    print ("Idź!")
    input("Wciśnij Enter aby wyjść")
else:
    print ("Niewłaściwe dane...")
    input("Wciśnij Enter aby wyjść")

jeszczeRaz = input("Czy jeszce raz...? Wpisz [TAK] ")
swiatlo = input("Jakie jest światło? (czerwone, zielone, pomaranczowe) ")
if  jeszczeRaz == "TAK":
    if  swiatlo == "czerwone":
        print ("Stój!!")
        input("Wciśnij Enter aby wyjść")
    elif swiatlo == "pomaranczowe":
        print ("Przygotuj się!")
        input("Wciśnij Enter aby wyjść")
    elif swiatlo == "zielone":
        print ("Idź!")
        input("Wciśnij Enter aby wyjść")
    else:
        print ("Niewłaściwe dane...")
        input("Wciśnij Enter aby wyjść")
else:
    print ("Bye")
    input("Wciśnij Enter aby wyjść")
    

    
