'''Pracujesz dla firmy odzieżowej, której celem jest
wypromowanie nowej kolekcji ubrań.
Firma ogłosiła konkurs, który ma na celu zdobywanie "lajków"
i "udostępnień" na Facebooku. Jeśli strona firmy otrzyma danego dnia
co najmniej 500 "lajków" i co najmniej 100 "udostępnień",
to ceny spadną o 10%. Na razie masz napisać fragment programu,
który rozstrzygnie czy warunki promocji są spełnione czy nie.
Jeśli już wiesz jak to zrobić "GO ON!", a jeśli chcesz, aby Cię
trochę pokierować - zajrzyj do kolejnych punktów:'''

# min_likes=500
# min_shares=100

num_likes=520
num_shares=50

# print ("Dzisiaj ", date.today()," otrzymaliśmy",num_likes,"lajków i",num_shares,"udostępnień, dlatego nie ma jeszcze rabatu. Potrzeba jeszcze", -(num_likes-500),"lajków i", -(num_shares-100),"udostępień")

from datetime import date
date.today()

if num_likes>=500 and num_shares>=100:
    print ("Dzisiaj ", date.today()," otrzymaliśmy",num_likes,"lajków i",num_shares,"udostępnień, dlatego ogłaszamy 10% upust")
#    print ("Dzisiaj otrzymaliśmy właściwą liczbę like i udostępnień, dlatego ogłaszamy 10% upust")
else:
    if num_likes<500:
        print ("Dzisiaj ", date.today()," otrzymaliśmy",num_likes,"lajków i dlatego nie ma rabatu 10%")

    else:
        print ("Dzisiaj ", date.today(),"otrzymaliśmy",num_shares,"udostępnień, dlatego nie ma 10% rabatu")
     
print ("-----------------")
