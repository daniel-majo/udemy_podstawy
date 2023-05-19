##liczba = input('Podaj liczbę: ')
##ver.1
##palindrom =''
##
##for litera in liczba:
##    palindrom = litera + palindrom
##print(palindrom)

##ver.2
##palindrom = liczba[::-1]
##print(palindrom)

#ver.3
##i = 0
##j = len(liczba) - 1
##
##while i < j and liczba[i] == liczba[j]:
##    i += 1
##    j -= 1
##
##if i >= j:
##    print('to jest palindrom')
##else:
##    print('to nie jest palindrom')

liczby = [2,3,5,12,100,24,87,15]

maks = liczby[0]
poz = 0

for i in range(len(liczby)):
    if liczby[i] > maks:
        maks = liczby[i]
        poz = i
print(f'Największa liczba {maks} na pozycji {poz}')
    





