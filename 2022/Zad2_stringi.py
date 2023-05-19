'''
Stwórz listę zawierającą 10 dowolnych liczb, a nastepnie przygotuj nową listę zawierającą wyłącznie
wartości podzielne przez 4 lub 6

'''
import random
numbers_list = []

for i in range(10):
    numbers_list.append(random.randint(1,50))
numbers_only_four_six = []

for number in (numbers_list):
    if (number%4 == 0) or (number%6 ==0):
        numbers_only_four_six.append(number)

print(f'Liczby wylosowane {numbers_list}')
print(f'Nowa lista{numbers_only_four_six}')