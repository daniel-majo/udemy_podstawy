#utworzenie obiektu dictionary słownika
chanels = {'Google' : 1480, 'Email':300, 'Natural Traffic':440, 'TV Spot':700}
print ('Dane kluczy i wartości słownika chanels:\n', chanels)

# Wyświetl wartość skojarzoną z kluczem "Email"
print ('Wartość klaucza Email:\n',chanels['Email'])

# utworzenie nowego słownika 'chanelsUpdate'
chanelsUpdate = {'Natural Traffic':520, 'News':600}

#Zaktualizuj słownik chanels wartościami z chanelsUpdate
chanels.update(chanelsUpdate)

# wyświetl klucze słownika chanels
print ('Klucze słownika:\n', chanels.keys())

# usuń wartość 'Email' ze słownika

print ('Usunięcie klucza "Email"',chanels.pop('Email'))

print (chanels)
