'''Dokuczałeś prowadzącemu ten kurs i dostajesz "za karę zadanie"
- musisz wyznaczyć sumy dwóch kolejnych liczb od 0 do 50, np
    0+1 = 1
    1+2 = 3
    2+3 = 5
    3+4 = 7 itd.

Wyjmij kartkę i licz lub:

- zadeklaruj zmienną number i przypisz jej wartość 1
- zadeklaruj zmienną previousNumber i przypisz jej wartość 0
- Napisz  pętlę while, która wykonywać się będzie tak długo, jak długo number
    jest mniejsze niż 50
- w pętli:
    - wyświetl sumę number i previous_number
    - do previous_number przypisz wartość number
    - zwiększ number o 1'''

number=1
previousNumber=0
while number <= 50:

    print (number + previousNumber)
    previousNumber=number
    number+=1
