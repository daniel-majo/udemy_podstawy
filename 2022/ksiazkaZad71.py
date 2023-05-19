'''
Napisz program, który wypełnia tablicę 5 elementmai będącymi wielokrotnością tej samej losowej liczby od 1 do 10,
Dla przykładu - jeśli wylosujemy 5, to pierwszy element będzie równy 5, nastepny - 10, kolejny 15 itd.
Następnie wymiesza tablicę, wyświetli pierwsze cztery elementy i poprosi użytkownika o odgadnięcie,
jaką ma ostatni element

#21 28 7 35
#Jaki jest ostatni element? 14
#Brawo!
1*5
2*5
3*5
4*5
'''
from random import randint, shuffle
list = []
value = randint(1,100)
multiplier = 1
for number in range(5):
    list.append(multiplier * value)
    multiplier +=1
shuffle(list)
print(f'4 elementy listy 5 elementowej {list[:4]}')
if int(input('Jaki jest ostatni element? ')) == list[4]:
    print('Brawo!')
else:
    print('Buuu')