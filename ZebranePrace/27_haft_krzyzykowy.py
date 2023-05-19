
#Czy wiesz, że polecenie: 5*'x'

#wyświetli xxxxx

'''Tym razem Twoja Babcia poprosiła Cię o wydrukowanie wzoru haftu krzyżykowego
w następującej postaci:

    x
    xx
    xxx
    xxxx
    xxxxx
    xxxxxx
    xxxxxxx
    xxxxxxxx
    xxxxxxxxx
    xxxxxxxxxx

Babcia woli jednak przechowywać te wzory w postaci skryptów Pythona zamiast
gotowych plików tekstowych ze wzorkiem, bo jak twierdzi "Skrypty zajmują w
komputerze mniej bajtów - cokolwiek by to było".

Napisz pętlę while, która wygeneruje taki napis składający się z liter 'x'
powielanych wiele razy.'''

i=1
imax=10

while i <= imax:
    print (i*'x')
    i+=1
else:
    print ('--------')
