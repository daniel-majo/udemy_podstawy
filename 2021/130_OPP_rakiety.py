'''
__init__ - initialization - inicjalizacja - czyli ustawienie
startowych wartości dla atrybutów

w innych językach __init__ to konstruktor
'''
from random import randint
class Rocket:
    def __init__(self):
        self.altitiude = 0 #wysokość rakiety
        self.speed = 0 #dorobić z prędkością

    def moveUp(self):
        self.altitiude += 1

rockets = list()

for _ in range(5):
    newRocket = Rocket()
    rockets.append(newRocket)
print(rockets)
#list komprehension
'''
rockets = [Rocket() for _ in range(5)]
'''
for _ in range(10):
    randomIndexToMove = randint(0,4)
    rockets[randomIndexToMove].moveUp()

for rocket in rockets:
    print(rocket.altitiude)