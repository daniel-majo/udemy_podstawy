'''
Dana jest zakodowana informacja w postaci tabeli:
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

Tym razem należy analizować po 3 wartości na raz.
Interesuje nas odnalezienie takich 3 liczb,
że pierwsza do kwadratu równa się drugiej,
a druga do kwadratu równa się trzeciej.

- analizujemy po 3 liczby na raz
- zmienna sterująca przyjmie wartość od zera do ....?'''

number=[8,18,2,4,16,5,25,4,22,3,3,5,3,9,81,11]
i=0
max=len(number)-2
while i<max:
    print(i,number[i],number[i+1],number[i+2])
    if number[i]**2==number[i+1] and number[i+1]**2==number[i+2]:
       print ('\t Znaleziono',number[i],number[i+1],number[i+2])

    i+=1
