liczby = []
##for liczba in range(100,471):
##    if (liczba % 7 ==0 and liczba % 5 !=0):
##        liczby.append(liczba)
'''
generator, dla wypisania wartości
'''

liczby = (
        liczba
        for liczba in range(100,471)
        if (liczba%7==0)
        if (liczba%5!=0)
        )
for liczba in liczby:
    print(liczba)
'''
lista
'''

liczby = [
        liczba
        for liczba in range(100,471)
        if (liczba%7==0)
        if (liczba%5!=0)
        ]

'''
zbiór
'''
print(liczby)
liczby = {
        liczba
        for liczba in range(100,471)
        if (liczba%7==0)
        if (liczba%5!=0)
        }

print(liczby)
