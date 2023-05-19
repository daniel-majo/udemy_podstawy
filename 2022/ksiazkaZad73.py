'''
Napiszmy razem algorytm, który sortuje tablicę.
Napisz algorytm sortowania bąbelkowego - jest to prosty algorytm sortujący. pośród wszystkich algorytmów sortujących znajduje się on w grupie tych którym sortowanie zajmuje najwięcej czasu. w przypadku naszych małych tablic będzie to jednak niezauważalne. algorytm bąbelkowy polega na tym, że tyle razy, ile tablica ma elementów (minus 1), wykonujemy następujące działanie dla elementów od pierwszego do przedostatniego: porównujemy kolejne elementy tablicy z tymi które są po nich. Jeśli następny element jest większy, to zamieniamy go i jego poprzedni element miejscami.
Tablica
| 8 | 5 | 10 | 1 |
Trzy razy będziemy porównywać po kolei pierwszy element z drugim, drugi z trzecim, a trzeci z czwartym.
Na początku sprawdzamy, czy  8 > 5?. Tak, więc zamieniamy miejscami elementy
| 5 | 8 | 10 | 1 |
Czy, teraz 8 > 10? Nie, więc zostaje.
| 5 | 8 | 10 | 1 |
Czy 10 > 1?. Tak, więc zamieniamy miejscami
| 5 | 8 | 1 | 10 |
Powtarzamy czynność porównywania pierwszego elementu z drugim, drugiego z trzecim, a trzeciego z czwartym jeszcze dwa raz, ponieważ musimy nasze porównania wykonać w sumie trzy razy dla całej naszej tablicy, bo są cztery elementy (-1)
Efekt sortowania krok ko kroku
Drugie powtórzenie
| 5 | 8 | 1 | 10 |
| 5 | 1 | 8 | 10 |
| 5 | 1 | 8 | 10 |
Trzecie powtórzenie
| 5 | 1 | 8 | 10 |
| 1 | 5 | 8 | 10 |
| 1 | 5 | 8 | 10 |

'''
from random import random, randint
a = 0 #nr elementu
t = [] #pusta lista
while a < 10:
    t.append(randint(1, 100))
    a += 1
print(t)

a = 0
while a < len(t) - 1:
    b = 0 #nr elementu
    while  b < len(t) - 1:
        if t[b] > t[b+1]:
            c = t[b]
            t[b] = t[b+1]
            t[b+1] = c
        b += 1
    a += 1
print(t)