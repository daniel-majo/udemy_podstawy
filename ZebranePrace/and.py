a = int(input("Podaj liczbę a: "))
b = int(input("POdaj liczbę b: "))

#if (a > 0):
    #if (b>0):
        #print("Liczby większe od zera")
#else:
   # print("Liczba równa zero")
    
if (a > 0 and b > 0):
    print("Liczby większe od zera")
elif (a < 0 and b > 0):
    print("Liczba a mniejsza od zera")
elif (a > 0 and b < 0):
    print("Liczba b mniejsza od zera")
elif (a ==0 and b ==0):
    print("Liczba a i b równa zero")
else:
    print("Liczba a i b mniejsza od zera")