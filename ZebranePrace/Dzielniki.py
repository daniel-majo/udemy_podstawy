liczba = input()

liczba = int(liczba)
##zmiana zmiennej liczba na liczbę integer

index = 1
while index<=liczba/2:
    if liczba%index==0:
        print(index)
    index = index
print(liczba)

