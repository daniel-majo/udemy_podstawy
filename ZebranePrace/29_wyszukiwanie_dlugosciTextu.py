'''
Tym razem w wejściowej liście znajdują się napisy:

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
'seven', 'eight', 'nine']

Twoim zadaniem jest znalezienie takich par kolejnych napisów z tej listy,
że długość pierwszego jest równa długości drugiego, np, długość napisu
"one" to 3, długość napisu "two" to 3, więc taka para powinna być odnaleziona.
Z kolei długość napisu 'two' to 3, a długość napisu "three" to 5,
więc taka para nie jest rozwiązaniem. Właściwie można znowu bazować
na poprzednich rozwiązaniach, ale:

- zmieniła się tabela wejściowa
- zmienia się warunek w if - to już nie są działania na liczbach
ale porównywanie długości napisów'''

texts = ['zero','one','two','three','four','five','six','seven','eight','nine']
i=0
max=len(texts)-1
while i<max:
    print(i,texts[i],texts[i+1])
    if len(texts[i])==len(texts[i+1]):
       print ('\t Znaleziono',texts[i],texts[i+1])

    i+=1
