'''Tym razem pomożemy lekarzom przeprowadzając wstępną analizę:
czy pacjent ma grypę, czy tylko przeziębienie
(zakładamy, że pacjentowi coś dolega, w tym zadaniu mamy tylko pomóc
zdiagnozować czy to jest grypa czy przeziębienie):'''

bolMiesni = False
goraczka = False
oslabienie = True
isMan = False

if bolMiesni and goraczka and oslabienie or isMan:
    print ("Podejrzenie grypy")
elif (bolMiesni or goraczka or oslabienie) and isMan:
    print ("Podejrzenie grypy")
elif oslabienie:
    print ("Odpocznij")
else:
    print ("Może jest Ci zimno")

print ("-----------")

if bolMiesni and goraczka and oslabienie or isMan and (bolMiesni or goraczka or oslabienie):
    print ("Podejrzenie grypy")
elif not (bolMiesni and goraczka) and oslabienie:
    print ("Odpocznij")
else:
    print ("Może jest Ci zimno")
