'''
random - z ang. losowy

random()  0<=x < 1 lub [0,1)

uniform(2.5,10.0) 2.5 <= x < 10.0 lub [2.5,10)
randrange(10)     z puli (1,2,3,4,5,6,7,8,9)
randrange(0,15,2) parzyste z puli (2,4,6,...14)

randint(0,4) [0,4]
'''
import random
'''x = 0

while x < 100:
    x = x + 1
    print(random.random())
'''    
'''
def will_weapon_hit (weaponChanceToHitPercentage):
    isHitChance = random.uniform(1,100)
    if (isHitChance < weaponChanceToHitPercentage):
        return "hit"
    else:
        return "not hit"
'''
'''
x = 0
listHit = []

while x < 100:
    x = x + 1
    listHit.append(will_weapon_hit(50))

listHit.count('hit') # zliczanie hitów

from collections import Counter
dictionaryHit = Counter(listHit)
'''
#-----------------
'''
x = 0

while x < 100:
    x = x + 1
    print(random.randrange(10))
'''
#-----------------
x = 0

while x < 100:
    x = x + 1
    print(random.randint(0,10))
