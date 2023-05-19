file = open("panstwa_i_stolice.txt", "w+") # "r" - tylko do oczytu, "w" - zapis, "w+" - do zapisu i odczytu, utworzenie pliku

panstwa_i_stolice ={'Polska':'Warszawa', 'Niemcy':'Berlin', 'Czechy':'Praga'}

#zapisanie do pliku
for panstwa, stolice in panstwa_i_stolice.items():
    file.write(panstwa + '-' + stolice + '\n')


file.close()


### odczyt z pliku

file = open("panstwa_i_stolice.txt")
for line in file.readlines():
    print(line.strip())# strip usuwa niepotrzebne znaki typu spacja i Enter
file.close()
