colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']

allCards=[]

for c in colors:
    for f in figures:
       allCards.append('%s - %s' % (c,f))
#print ('Karty wylosowane to:',allCards)

import random

random.shuffle(allCards)
print ('Karty potasowane to:\n',allCards)

player1=[]
player2=[]
print("\n-------------------------------------------- pierwszy sposob ---------------------------------------- \n")
max = len(allCards)

for i in range(max):
    if i%2==0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

print ('Karty gracza player1:\n',player1,len(player1))
print ('Karty gracza player2:\n',player2,len(player2))
print("\n-------------------------------------------- drugi sposob ---------------------------------------- \n")

player_1=allCards[:12]
player_2=allCards[12:]

print ('Karty gracza player1:\n',player_1,len(player_1))
print ('Karty gracza player2:\n',player_2,len(player_2))

##colors = ['Hearts','Diamonds','Clubs','Spades']
##figures = ['Ace','King','Queen','Jack','10','9']
## 
##allCards = []
##for c in colors:
##    for f in figures:
##        allCards.append("%s - %s" % (c, f))
## 
##print(allCards)
## 
##import random
## 
##random.shuffle(allCards)
##print(allCards)
## 
##player1 = []
##player2 = []
## 
##max = len(allCards)
##for i in range(max):
##    if i % 2 == 0:
##        player1.append(allCards[i])
##    else:
##        player2.append(allCards[i])
## 
##print('-------PLAYER 1--------')
##print(player1)
## 
##print('-------PLAYER 2--------')
##print(player2)              
   

