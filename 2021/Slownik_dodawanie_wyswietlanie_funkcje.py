panstwa_stolice = {}

panstwa_stolice["Polska"] = ("Warszawa",37.79)
panstwa_stolice["Niemcy"] = ("Berlin", 83.03)

'''
tworzenie funkcji
'''

def pokaz_kraj(stolica):
    panstwo_stolice = panstwa_stolice.get(stolica)
    print()
    print(stolica)
    print("--------")
    print("Stolica: " + panstwo_stolice[0])
    print("Liczba mieszkańców (mln): " + str(panstwo_stolice[1]))

for stolice in panstwa_stolice.keys():
    print(stolice)

stolica = input("Informacja o jakim kraju chcesz wyswietlić? ")

pokaz_kraj(stolica)


