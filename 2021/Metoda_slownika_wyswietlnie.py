slownik = {'Polska':'Warszawa', 'Niemcy':'Berlin','Francja':'Paryż'}
##for key in slownik:
##    print(slownik[key])
'''
wyświetlenie treści po kluczu
'''
for kraj in slownik.keys():
    print('Klucz ',kraj)
'''
wyświetlenie treści po wartości
'''
for kraj in slownik.values():
    print('Wartość ',kraj)

'''
wyświetlenie treści słownika
'''
for kraj, stolica in slownik.items():
    print(kraj, '-', stolica)

'''
wyświetlenie wartości po kluczu
'''

#print(slownik['USA'])# w przypadku nie występowania w słowniku zwróci błąd

print(slownik.get('USA'))# w przypadku nie występowania w słowniku zwróci None

'''
podmiana wartości z Warszawa na Kraków
'''
slownik['Polska'] = 'Kraków'
print(slownik)
