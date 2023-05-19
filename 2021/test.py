#od 100 do 0, 5, 4, 3,2,1
print("Sumowanie dowolnych kolejnych liczb ")
liczba = int(input("Podaj ile liczb chcesz zsumować: "))
suma = 0


while liczba >0:
    
    liczba-=1
    suma=suma+liczba
    print(suma)

