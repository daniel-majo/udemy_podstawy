'''
Ciąg Fibonacciego to ciąg rozpoczynający się od 0 i 1 a każda kolejna liczba
to suma dwóch poprzednich, np:

0
1
0+1 = 1
1+1 = 2
1+2 = 3
2+3 = 5
....

Korzystając z pętli for napisz program, który wyliczy fibonacciIterations=20
pierwszych elementów ciągu Fibonacciego

Wskazówka:
-zadeklaruj 3 dodatkowe zmienne a1, a2 i a3.
Początkowo a1=0 a a2=1. a3 będziesz wyliczać jako sumę a1 i a2.
W pętli trzeba też będzie zmieniać wartość a1 na a2 oraz a2 na a3
'''

a1 = 0
a2 = 1
a3 = 0
fibonacciIterations=20

for i in range(0,20):
       print ('Pęla',i,'wartość ciągu',a3)
       a1=a2
       a2=a3
       a3=a1+a2
