lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# len() w Python pobiera długosc, a wiec i liczbę elementow
ilosc_liczb = len(lista_liczb)

suma = 0
srednia = 0
for liczba in lista_liczb:
    suma = suma  + liczba
    srednia = suma /ilosc_liczb
print ('Srednia z liczb to: ' + str(srednia))
