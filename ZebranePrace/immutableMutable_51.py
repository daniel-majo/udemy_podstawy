'''
obiekt to zmienna, która ma więcej możliwości
można wywołać na nim „funkcje”
może mieć więcej niż jedną wartość
obiekt immutable: bool, int, str, float, tuple
immutable – niezmienne
mutable - zmienny

zmiana miejsca wskazywania na nowy adres na inny obiekt

'''

c=5

def add(c, amount = 1):
    print(id(c)) #drukowanie miejsca przechowywania danych
    print(c)
    c = c + amount
    print(id(c))
    print(c)
add(c)
#print(id(c))
#print(c)

listSample = [1, 4, 512, 24]


def append_element_to_list(listka, element):
    print(id(listka))
    listka.append(element)
    print(id(listka))

print(id(listSample))
append_element_to_list(listSample, 5)
