'''
Program, który policzy sumę wszsystkich liczb od 1 do podanej liczby przez użytkownika
dla 5
1+2+3+4+5
zwróci 15


range(6)
1,2,3,4,5




'''
# 1. opcja funkcji i pętli for
'''
def sumuj_do(liczba):
    suma = 0
    for liczba in range(1,liczba+1):
        suma = suma + liczba
    return suma

print(sumuj_do(5))
'''
# 2. opcja generatora
def sumuj_do2(liczba):#lista
    return sum([liczba for liczba in range(1,liczba+1)])

def sumuj_do3(liczba):#set
    return sum({liczba for liczba in range(1,liczba+1)})

def sumuj_do4(liczba):#generator
    return sum((liczba for liczba in range(1,liczba+1)))

print(sumuj_do2(25))
print(sumuj_do3(25))
print(sumuj_do4(25))

# 3. opcja ciąg arytmetyczny
def sumuj_do5(liczba):
    return (1 + liczba)/2*liczba
#   (pierwsza liczba + ostatnia liczba)2 * ilość elementów
print(sumuj_do5(25))

    
##i = 0
##suma = 0
##j = int(input("Podaj liczbę do której ma wyliczyć program"))
##
##while (j > i):
##    suma = suma + j
##    j=j-1
##print(suma)

