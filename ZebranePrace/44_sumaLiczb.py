'''
Dana jest liczba całkowita dodatnia number = 20730906.
Oblicz sumę cyfr tej liczby.

Wskazówka 1:

-utwórz pomocniczą zmienną, która będzie podlegała modyfikacji podczas pracy
programu

-warunkiem pętli może być sprawdzanie, czy ta pomocnicza zmienna jest >0

-aby wyliczyć ostatnią cyfrę podziel pomocniczą zmienną modulo (operator %) 10

-aby usunąć ostatnią cyfrę z pomocniczej zmiennej podziel ją cąłkowiicie
( operator // )  przez 10 i wynik zapisz w tej samej pomocniczej zmiennej

Wskazówka 2:

Skorzystaj z tego opisu, jeżeli nadal nie masz pomysłu na rozwiązanie.
Ten opis, to jakby słowne opowiedzenie tego co robi program:

    Mamy liczbę 20730906 zapisną, a jakże inaczej w systemie DZIESIĘTNYM.

    Kiedy tą liczbę podzielę modulo (symbol działania %) przez 10
    (dzielenie modulo zwraca resztę z dzielenia) to dostaniemy 6
    - czyli ostatnią cyfrę.

    Potem ta ostatnia cyfra już mnie nie obchodzi. Więc dzielę bez reszty
    (symbol działania //) przez 10. W wyniku dostaję więc liczbę 2073090.

    I od początku:

    Mamy liczbę 2073090 i dzielę ją modulo % przez 10. Zwrócona reszta to 0

    Teraz ostatnia cyfra już mnie nie obchodzi, więc dzielę bez reszty //
    przez 10. W wyniku dostaję liczbę 207309.

    I od początku:

    Mamy liczbę 207309 i dzielę ją modulo % przez 10. Zwrócona reszta to 9

    Teraz ostatnia cyfra już mnie nie obchodzi, więc dzielę bez reszty //
    przez 10. W wyniku dostaję liczbę 207309

    i tak dalej, aż dojdę do zera.
'''

number = 20730906

tmp_number = number

suma = 0

while tmp_number > 0:
    reszta = tmp_number%10
    suma += reszta
    tmp_number=tmp_number//10
       
else:
    
    print ("Suma liczb, liczby %d to %s" %(number,suma))
            
        
            

        
