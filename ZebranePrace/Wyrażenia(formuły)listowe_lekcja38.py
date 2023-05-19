'''
Wyrażenia (formuły) listowe - Transformacja
'''
liczby = [1,2,3,4,5,6]

potegiDwojki = []
for element in liczby:                      #skąd pobierane
    potegiDwojki.append(element**2)         #co się wykonuje

liczbyParzyste= []
for element in liczby:                      #skąd pobierane     można dodać range(7)
    if (element %2 ==0):                    #na postawie czego
        liczbyParzyste.append(liczby)       #co się wykonuje

# inna wersja wykonania powyższej operacji

potegiDwojki2 = [element**2                 #co się wykonuje
                 for element in liczby      #skąd pobierane
                 ]

liczbyParzyste2 = [element                  #co się wykonuje
                   for element in liczby    #skąd pobierane
                   if (element%2==0)        #na postawie czego
                   ]

# [co_zrobic_na_elemencie | for element in stara_lista | warunek_oparty_na_elemencie]
