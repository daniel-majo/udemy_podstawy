# funkcja jeżeli
a=4
b=6
c=8

if a>b and a>c:
    print ('a jest większa od b i c, bo: ')
    print (a,' jest większa od', b)
elif b==c:
    print ('b jest rowne c')
    print (b,' jest rowne', c)
else:
    print ('b jest większa od a, bo:')
    print (b,' jest większa od', a)

''' Należy pamiętać że a = b to przypisanie, natomiast a == b to porównanie.
Pominięcie jednego znaku równości jest częstym błędem.'''