'''
Dany masz słownik:

dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'} 

Wyświetl zestawienie w postaci (kolejność nie jest istotna):

    A - 80%-100%
    B - 60%-80%
    C - 50-60%
    D - less then 50%
'''

dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'}
for litery in dictionary.keys():
    
    print (litery,'-',dictionary[litery])
