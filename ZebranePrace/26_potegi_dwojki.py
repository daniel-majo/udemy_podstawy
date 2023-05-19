'''Śni Ci się koszmar. Dziecko kuzynki zafascynowane informatyką  prosi Cię
o wymienienie kolejnych potęg dwójki. Postanawiasz znowu skorzystać z Pythona.
Napisz pętlę while, która dla liczby x od 0 do 16 wyznaczy
wartość dwa do potęgi x.'''

start = 0
end = 16
x=start

while x <= end:
    print ("2 do potęgi",x,"=",2**x)
    x+=1
else:
    print ("--------")
