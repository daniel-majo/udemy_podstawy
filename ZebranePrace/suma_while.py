#od 100 do 0, 5, 4, 3,2,1
##print("Sumowanie dowolnych kolejnych liczb ")
##
##liczba = int(input("Podaj ile liczb chcesz zsumować: "))
##suma = 0
##
##
##while liczba >0:
##    
##    liczba-=1
##    suma=suma+liczba
##    print(suma)



##
##suma = 0
##i = 0
##
##while i < 4:
##    liczba = int(input("Podaj liczbę: "))
##    suma = suma + liczba
##    i+=1
##print("Suma: ",suma)

#Liczby podzielne przez 5 i niepodzielne przez 7

for i in range(200):
    if (i%5==0 and not(i%7==0)):
        print("Liczba podzielna przez 5 i niepodzielna przez 7 to: ",i)
