"""
Napisz krótką grę w której masz 5 ruchów w jedną stronę poprzez KOMNATĘ.
Za każdym razem masz szansę spotkać po drodzę skrzynkę lub NIC.
Skrzynki mają różne kolory.
Kolor skrzynki oznacza jak rzadka jest ta skrzynka.

zielona - 75%
pomarańczowa - 20%
fioletowa - 4%
złota (legendarna) - 1%

Ustaw, że jest 40% szansy, że nie spotkasz niczego. 60%, że będzie skrzynka.

Ustaw złoto jako to co może "wypaść" ze skrzynki:
zielony - 1000,
pomaranczowy - 4000,
fioletowy - 9000,
zlota - 16000

1 1 0+1
4 2 1 +1
9 3 2+1
16 4 3 +1

Pamiętaj o:
1) czystym kodzie
2) nazywaniu zmiennych tak by bylo samoopisujace sie
3) spróbuj napisać program po angielsku

"""
import random
from enum import Enum
Event = Enum('Event',['Chest','Empty'])

eventDictionary = {                 #słownik zdarzeń
                    Event.Chest: 0.6,
                    Event.Empty: 0.4
                    }
evenList = list(eventDictionary.keys())
evenProbability = list(eventDictionary.values())# prawdopodobieństwo wystąpienia zdarzeń

Colours = Enum('Colours', {'Green':'zielony'
                            }
               )

gameLength = 5 # ilość kroków
print("Witaj w mojej gre KOMNATA")
print('''
Możesz wykonać tylko 5 kroków,
zobaczymy, ile złota zdobędie do końca gry
    ''')
while gameLength > 0:
    gameAnswer = input("Czy chcesz iść do przodu?")
    if (gameAnswer == "yes"):
        print("Dobrze, zobaczmy co otrzymałeś...")
        drawnEvent = random.choices(evenList,evenProbability)[0]
        if (drawnEvent == Event.Chest):
            print("Wylosowałeś skrzynkę")
        elif (drawnEvent == Event.Empty):
            print("NIC nie wylosowałeś, masz pecha")
        
    else:
        print("Możesz iść tylko do przodu...")
        continue
    
    gameLength = gameLength - 1


