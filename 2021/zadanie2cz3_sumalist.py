'''
Przygotuj funkcję, która odbierze od użytkownika dwie listy i zwróci nową listę zawierającą sumy poszczególnych elementów
np. 
[1, 2, 3] i [4, 5, 6] zwróci [5, 7, 10]
'''
list1 = [1, 2, 3]
list2 = [4, 5, 6]

def sum_list(list1: list, list2: list) -> list:
    result = []
    for element1, element2 in zip(list1, list2):
        result.append(element1 + element2)

    return result

print(sum_list(
    [1, 2, 3],
    [4, 5, 6]
))