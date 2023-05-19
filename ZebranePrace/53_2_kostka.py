'''Rzuć pięcioma kostkami:


    - zadeklaruj zmienną dices jako pustą listę

    - pięć razy wylosuj liczbę z zakresu min do max i wynik dopisz
    do listy dices

    - posortuj listę dices

    - wyświetl zawartość zmienej dices  '''

import random

dices=[]
min=1
max=6
    
for i in range(5):
    dices.append(random.randint(min,max))
dices.sort()
    
   
print (dices)
