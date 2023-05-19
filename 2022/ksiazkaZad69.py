'''
Napisz program, który tworzy 3 elementy tablicy jako losowe liczby od 1 do 80,
a nastepnie wypisuje liczby z tej tablicy i wyświetla je.
'''
import random
numbers_table = [random.randint(1,80), random.randint(1,80), random.randint(1,80)]
a = 0
while a < 3:
    print(numbers_table[a])
    a +=1




# numbers_table = []
# number = 0
# while number < 3:
#     numbers_table.append(random.randint(1,80))
#     number +=1
# print(numbers_table)