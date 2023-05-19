'''
Mierzenie wydajnści skryptu
'''
import time
# 1. opcja funkcji i pętli for

def sumuj_do(liczba):
    suma = 0
    for liczba in range(1,liczba+1):
        suma = suma + liczba
    return suma
start=time.perf_counter()
print(sumuj_do(256))
end=time.perf_counter()
print(end-start)

# 2. opcja generatora
def sumuj_do2(liczba):# lista
    return sum([liczba for liczba in range(1,liczba+1)])

def sumuj_do3(liczba):#set
    return sum({liczba for liczba in range(1,liczba+1)})

def sumuj_do4(liczba):#generator
    return sum((liczba for liczba in range(1,liczba+1)))

start=time.perf_counter()
print(sumuj_do2(256))
end=time.perf_counter()
print(end-start)

start=time.perf_counter()
print(sumuj_do3(256))
end=time.perf_counter()
print(end-start)

start=time.perf_counter()
print(sumuj_do4(256))
end=time.perf_counter()
print(end-start)
# 3. opcja ciąg arytmetyczny
def sumuj_do5(liczba):
    return (1 + liczba)/2*liczba
#   (pierwsza liczba + ostatnia liczba)2 * ilość elementów
start=time.perf_counter()
print(sumuj_do5(256))
end=time.perf_counter()
print(end-start)

def finish_timer(start):
    end = time.porf_counter()
    return end-start
print(finish_timer(start))

##i = 0
##suma = 0
##j = int(input("Podaj liczbę do której ma wyliczyć program"))
##
##while (j > i):
##    suma = suma + j
##    j=j-1
##print(suma)

