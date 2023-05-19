'''W tym zadaniu obliczysz silnię. Silnia  to działanie matematyczne,
które dla liczby n wyznacza wartość mnożąc przez siebie wszystkie
liczby naturalne mniejsze lub równe n. Symbol oznaczający silnię to wykrzyknik,
np.:

2! = 1*2 =2
3! = 1*2*3 = 6
4! = 1*2*3*4 = 24

Zmienna i ma wartość 10. Korzystając z pętli for wyznacz wartość silnia i'''

        
i = 10
wynik = 1
 
for j in range(1,i+1):
    wynik *= j
 
print(i,'! =',wynik)
 
print('------------')
