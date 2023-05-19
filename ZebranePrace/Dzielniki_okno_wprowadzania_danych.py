liczba = input()

liczba = int(liczba)
##zmiana zmiennej liczba z tekstu na liczbę integer
##można zapisac w skrocie tj. liczba = int(input())

index = 1
while index<=liczba/2:
    if liczba%index==0:
        print(index)
    index = index + 1
print(liczba)

