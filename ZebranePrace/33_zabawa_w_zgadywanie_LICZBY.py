
import random
my_number=random.randint(0,20)
quess=-1
trials=0
print ("Spróbuj odgadnąć liczbę za kresu od 0 do 20")

while quess!=my_number:
    quess=int(input("Podaj liczbę "))
    trials+=1
    if quess==my_number:
        print ("Brawo!! Odgadłeś moją liczbę")
#        trials+=1
    elif quess>my_number:
        print ("Niestety nie!! Moja liczba jest mniejsza")
#        trials+=1
    else:
        print ("Niestety nie!! Moja liczba jest większa")
#        trials+=1

print ("Ilość prób: ",trials)
