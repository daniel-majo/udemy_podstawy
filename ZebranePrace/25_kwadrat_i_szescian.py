'''Śni Ci się koszmar.
Twój nauczyciel matematyki kazał Ci wypisać liczby od 1 do 13
i dla każdej liczby wyliczyć jej kwadrat i sześcian.
Ponieważ nauczyciel nie zabronił używać Pythona, napisz pętlę,
która dla liczb od 1 do 13 wyświetli kwadrat i sześcian tej liczby'''

i = 1
imax = 13

while i <= imax:
    print ("Kwadrat liczby",i,"wynosi",i**2)
    print ("Sześcian liczby",i,"wynosi",i**3)
    i+=1
else:
    print ("---------")
