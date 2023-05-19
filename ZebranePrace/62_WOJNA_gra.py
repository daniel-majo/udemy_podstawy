colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards=[]

for c in colors:
    for f in figures:
        aCard=f.copy()
        aCard['colors']=c
        allCards.append(aCard)

#print ('Karty wylosowane to:',allCards)

import random

random.shuffle(allCards)
print ('Karty potasowane to:\n',allCards)

player1=[]
player2=[]
print("\n------------------------------------------------------------------- \n")
max = len(allCards)

for i in range(max):
    if i%2==0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

print ('Karty gracza player1:\n',player1,len(player1))
print ('Karty gracza player2:\n',player2,len(player2))

while len(player1)>0 and len(player2)>0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    if card1["Power"]==card2["Power"]:
        player1.append(card1)
        player2.append(card2)

        print ('=EQUAL \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    elif card1["Power"]>card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        print ('Player-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    else:
        player2.append(card2)
        player2.append(card1)
        print ('Player-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
if len(player1)>0:
    print ('PLAYER 1 is WON !!')
else:
     print ('PLAYER 2 is WON !!')      
        
