'''
Dana jest zakodowana informacja w postaci tabeli
numbers = [8,18,2,4,16,5,25,4,22,3,3,5,3,9,81,11]
Trzeba odnaleźć takie dane kolejne liczby, że druga jest kwadratem pierwszej.
'''
numbers = [8,18,2,4,16,5,25,4,22,3,3,5,3,9,81,11]
# i = 0
# max = len(numbers) - 1

# while i < max:
#     print(f'{i} para, {numbers[i]}, {numbers[i+1]}')
#     if numbers[i]**2 == numbers[i+1]:
#         print(f'Znaleziona para liczb {numbers[i]} - {numbers[i + 1]}')
#     i += 1
'''
Odnalezienie 3 takich liczb, że pierwsza do kwadratu równa się drugiej, a druga do kwadratu równa się trzeciej
'''
# i = 0
# max = len(numbers) - 2
# while i < max:
#     print(f'{i} para, {numbers[i]}, {numbers[i+1]}, {numbers[i+2]}')
#     if numbers[i] ** 2 == numbers[i+1] and numbers[i+1] ** 2 == numbers[i + 2]:
#         print(f'Znaleziono liczby {numbers[i]} - {numbers[i + 1]} - {numbers[i + 2]}')
#     i += 1