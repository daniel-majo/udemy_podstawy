'''
Dana jest zakodowana informacja w postaci tabeli:
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

Trzeba odnaleźć takie dwie kolejne liczby, że druga jest kwadratem pierwszej.
W tym celu:

- trzeba wykonać analizę po dwa elementy na raz
- zmienna sterująca i przyjmie wartość od zera do ..... ?
- przy pomocy pętli while i sterującej nią zmiennej i analizuj po dwie wartości z listy na raz
- wyświetl analizowane wartości
- jeżeli pierwsza z nich do kwadratu jest równa drugiej, to wyświetl napis "FOUND"'''

number=[8,18,2,4,16,5,25,4,22,3,3,5,3,9,81,11]
i=0
max=len(number)
while i<max:
    print(i,number[i],number[i+1])
    if number[i]**2==number[i+1]:
       print ('\t Znaleziono',number[i],number[i+1])

    i+=1
