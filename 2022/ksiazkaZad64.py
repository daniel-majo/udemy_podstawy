
'''
Program losuje libzy z zakresu od 0 do 100. Jak wylosuje 50 przestaje działać
'''
import random
import time

a = random.randint(0,100)
id = 0
while a != 42:
    a = random.randint(0,100)
    #time.sleep(1)
    print(f'Losowanie {id} {a}')
    id +=1
    

print('Koniec pętli')