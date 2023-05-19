'''
listy'''

##imiona =['Daniel','Karolina','Mariola','Elżbieta']
##        # 0         1           2       3   numerowanie indexu od początku
##        #-4         -3          -2      -1  numerwoanie indexu od końca
##liczby = [1,4,5,6,7]
##mieszane = ['Karol', 1, 5, "Włocławek"]
##
###lista.append(4)
###lista.append(imiona))
##
##print(imiona)
##imiona[0]="Lidia"   # podmiana indexu 0 z Daniel na Lidia
##
##for imie in imiona:
##    print(imie)

#len()-długość listy length
#.append - dodać na końcu listy
#.extend - rozszerzyć
#.insert(index, co) - wstawić
#.index - index danego el.
#sort(reverse=False) - sortuj rosnąco domyślnie, chcąc posortować malejąco reverse=True
#max()
#min()
#.count - ile razy coś wystąpi
#.pop - usuń ostatni el.
#.remove - usuń pierwsze wystąpienie
#.clear - wyczyść listę
#.reverse - zmień kolejność

lista1 = [1,3,98,-15,22]
lista2 = ["Daniel","Elżbieta"]

#print(lista1 + [14])#dodać tylko na czas wyświetlania
lista1.append(14)
lista1.extend([21,36,3,99,16])# rozszerzenie o elementy podane we własciwości funkcji

print(lista1.index(98)) #sprawdzenie indexu dla wartości 98

#print(lista2)
lista2.insert(1,"Zuza") #dodanie w indexie 1 napisu Zuza

#print(len(lista1))
#print(lista1)
#print(lista2)

numbers = [2, 5, 2, 10, 15, 6]
numbers.insert(3,11)
numbers.append(4)
print(len(numbers))


