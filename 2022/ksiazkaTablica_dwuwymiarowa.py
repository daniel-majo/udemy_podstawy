'''
Tablica dwuwymiarowa
|1|2|3|
|4|5|6|

Element 1 ma indekxy [0][0]
Element 2 ma indeksy [0][1]
Element 3 ma indekxy [0][2]
Element 4 ma indeksy [1][0]
Element 5 ma indekxy [1][1]
Element 6 ma indeksy [1][2]
'''

# t = [[1,2,3],[4,5,6]]
# print(t)
# print()
# print(f'Element w drugim wierszu i drugiej kolumnie {t[1][1]}')

'''
Utwórz pustą listę dwuwymiarową 3 na 3, z losową wartością True lub False
'''
import random
t = [[],[],[]]
i = 0
while i < 3:
    j = 0
    while j < 3:
        t[i].append(bool(random.randint(0,1)))
        j += 1
    i += 1
print(t)