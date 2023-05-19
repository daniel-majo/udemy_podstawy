'''
choice - zwraca losowy element
choices - zwraca listę elementów i ma większe możliwości
'''
import random
movieList=["Tytuł 1","Tytuł 2","Tytuł 3","Tytuł 1"]

event = ["śmierć", "wygrana", "przegrana", "utrata złota", "utrata życia"]

nagrodaZeSkrzynki = ["zielona", "pomarańczowa", "purpurowa", "legendarna"]

print(random.choice(movieList))

from collections import Counter
print(Counter(random.choices(nagrodaZeSkrzynki, [1,2,3,4], k=100)))
