'''
Napiszesz funckję, która zasymuluje jak działa lotto,
tzn. wybierzecz 6 UNIKALNYCH liczb z 49

sample - próbka/przykład
'''
import random
'''
cardList =["9","9","9","9",
           "10","10","10","10",
           "Jack","Jack","Jack","Jack",
           "Queen","Queen","Queen","Queen",
           "King","King","King","King",
           "Ace","Ace","Ace","Ace",
           "Joker","Joker"]
random.shuffle(cardList)
'''
''' [0,1,2,...49]'''

#wersja z pętlą
'''
komora = []
def choose_random_numbers(amount, total_amount):
    x=0

    while x < amount:
        number= random.randint(amount,total_amount)
        if number not in komora:
            komora.append(number)
        else:
            continue
        x = x + 1
choose_random_numbers(6, 49)
print(set(komora))
'''    


# wersja z sample
'''

def choose_random_numbers(amount, total_amount):
    print(random.sample(range(total_amount+1), amount))

choose_random_numbers(6, 49)
'''


# tasowanie kart i rozdawanie 5 kart dla kązdego gracza
'''
lista_kart1=[]
lista_kart2=[]

def chooseCardsForTwoPlayers(amount_card, name1, name2):
    cardList = ["9", "9", "9", "9",
                "10", "10", "10", "10",
                "Jack", "Jack", "Jack", "Jack",
                "Queen", "Queen", "Queen", "Queen",
                "King", "King", "King", "King",
                "Ace", "Ace", "Ace", "Ace",
                "Joker", "Joker"]
    random.shuffle(cardList)

    while amount_card > 0:
        karta1 = cardList.pop()
        karta2 = cardList.pop()

        lista_kart1.append(karta1)
        lista_kart2.append(karta2)
        amount_card = amount_card - 1
    print("Lista kart",name1, lista_kart1)
    print("Lista kart",name2, lista_kart2)
    print(cardList)# reszta kart nie wylosowanych

chooseCardsForTwoPlayers(5, 'Daniel', 'Ela')
'''




        
