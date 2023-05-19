
'''
Program losuje liczby z zakresu od 1 do 100. Jak wylosuje 50 przestaje działać
'''
import random

id = 0
while True:
    a = random.randint(1,100)
    print(f'Losowanie {id} {a}')
    if a == 50:
        id +=1
        break
 
print('Koniec pętli')