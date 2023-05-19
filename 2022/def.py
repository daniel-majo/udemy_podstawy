def podaj_liczby(n):
    lista=[]
    sum=0

    for i in range(0,n):
        x = int(input("Podaj liczbę "))
        lista.append(x)
        sum +=x
    print(lista)
    return sum

print(podaj_liczby(2))
