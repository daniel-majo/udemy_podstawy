'''
Napisz program, który pobiera od użytkownika liczbę,
a następenie w konsoli wyświetla wyniki mnożenia tej liczby przez inne liczby od 1 do 10
'''
a = int(input('Podaj liczbę: '))
liczba = 1
while liczba < 11:
    print(a * liczba)
    liczba += 1




# for liczba in range(1,11):
#     iloczyn = liczba * a
#     print(iloczyn)