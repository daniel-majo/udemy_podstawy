'''Masz liczbę rzeczowników i przymiotników:

    list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
    list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

Utwórz pętlę for iterującą przez listę rzeczowników i zagnieżdżoną
w niej pętlę for iterującą przez listę przymiotników.
Wyświetl wszystkie pary przymiotnik - rzeczownik'''

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for rzeczownik in list_noun:
    for przymiotnik in list_adj:
        print(przymiotnik,' - ', rzeczownik)
