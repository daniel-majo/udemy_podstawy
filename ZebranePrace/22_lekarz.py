'''Tym razem pomożemy lekarzom przeprowadzając wstępną analizę:
czy pacjent ma grypę, czy tylko przeziębienie
(zakładamy, że pacjentowi coś dolega, w tym zadaniu mamy tylko pomóc
zdiagnozować czy to jest grypa czy przeziębienie):'''
bolMiesni = True
goraczka = True
oslabienie = True

print("Podejrzenie grypy" if bolMiesni and goraczka and oslabienie else "Grypa jest mało prawdopodobna")

