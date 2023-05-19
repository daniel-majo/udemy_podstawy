'''
Program, który pozwoli użytkownikowi:
1. Dodawać nowe definicje
2. Szukać istnijących definicji
3. Usuwać wygrane definicje
'''

definicje = {}
while (True):
    print("1.Dodaj nowe definicje")
    print("2.Znajdź definicję")
    print("3.Usuń definicje")
    print("4.Wyjście")


    wybor = input("Podaj swój wybór ")


    if wybor == "1":
        klucz = input("Podaj klucz(słowo) do wprowadzenia: ")
        definicja = input("Podaj definicję: ")
        definicje[klucz] = definicja
        print("Definicja dodana pomyślnie")
    elif wybor =="2":
        klucz = input("Podaj klucz, którego szukasz: ")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Nie znaleziono definicji o nazwie", klucz)
    elif wybor =="3":
        klucz = input("Podaj klucz, który chcesz usunąć: ")
        if klucz in definicje:
            del definicje[klucz]
            print("Usunięto definicję o nazwie", klucz)
        else:
            print("Nie znaleziono definicji o nazwie", klucz)
    elif wybor =="4":
        break

    else:
        print("Podałeś niewłasciwe dane, więc kończymy")
        input("wciśnij Enter")

