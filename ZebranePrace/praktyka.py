wybor = -1

lista =[]
#lista.append("Wynieść śmieci")
#lista.append("Zmyć naczynia")

def usun_zadanie():
    zadanie_index = int(input("Podaj index zadania do usunięcia: "))

    if zadanie_index>0 or zadanie_index > len(lista)-1:
        print("Zadanie o tym indexie nie istnieje")
        return
    
    lista.pop(zadanie_index)
    print("Zadanie zostało usunięte! ")
    
def pokaz_zadania():
    zadanie_index = 0
    for zadanie in lista:
        print(zadanie + " ["+str(zadanie_index)+"]")
        zadanie_index+=1

def dodanie_zadania():
    zadanie = input("Podaj zadanie: ")

    lista.append(zadanie)
    print("Zadanie zostało dodane! ")

def zapis_do_pliku():
    file = open("zadania.txt", "w")
    for zadanie in lista:
        file.write(zadanie+"\n")
        print("Zadanie zostało zapisane! ")
    file.close()
def ladowanie_zadan_z_pliku():

    try:
        
        file=open("zadania.txt")

        for line in file.readlines():
            lista.append(line.strip())

        file.close()
    except FileNotFoundError:
        return

ladowanie_zadan_z_pliku()

while wybor!=5:
    if wybor ==1:
        pokaz_zadania()
        
    if wybor == 2:
        dodanie_zadania()
        
    if wybor == 3:
        usun_zadanie()
    if wybor == 4:
        zapis_do_pliku()    
        
    print()
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Wyjdź")
    print()

    wybor = int(input("Dokonaj wyboru: "))
    print()
