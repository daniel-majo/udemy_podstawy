'''Chcesz wyznaczyć wartości silnia dla liczb od 1 do 10.
Napisz pętlę for iterującą przez wartości od 1 do 10,
a w tej pętli for wyznaczaj silnię dla każdej z tych liczb'''

        

x = 10
 
for i in range(1,x+1):
 
    result = 1
    
    for j in range(1,i+1):
        result *= j
 
    print(i, result)
 
print('------------')
