"""
Ćwiczenie
Wczytaj imiona i naziwska z pliku o nazwie:
imionanazwisko.txt

1) rozdziel je tak, by powstała lista krotek, gdzie
wewnętrzne krotki to pary imiona/nazwiska
2) zapisz imiona do pliku imiona.txt
3) nazwiska do nazwisko.txt

"""
namesandsurnames = []

with open("imionanazwiska.txt","r", encoding="UTF-8") as file:
    for line in file:
        namesandsurnames.append(tuple(line.replace('\n','').split(" ")))

with open("imiona.txt","w", encoding="UTF-8") as file:
    for items in namesandsurnames:
        file.write(items[0]+"\n")

with open("nazwiska.txt","w", encoding="UTF-8") as file:
    for items in namesandsurnames:
#        if len(items)==2:
#            file.write(items[1]+"\n")
#        else:
#            file.write("\n")
        try:
            file.write(items[1]+"\n")
        except IndexError:
            file.write("\n")
