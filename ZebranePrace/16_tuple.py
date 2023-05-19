# lista tuple
marketing = ('loyality program','client promotion','market research')
print ('Lista tuple\n',marketing)

# konwersja tuple na list
listmarketing=list(marketing)
print ('Lista tuple przekonwerstowana na liste\n',listmarketing)

# dodanie do listy elementu 'public relations'
listmarketing.append('public relations')
print ('Lista z dodatkowym elementem\n',listmarketing)

# wyświetlenie pozycji nr 3
print ('Wyświetlanie pozycji nr 3\n',listmarketing[3])
print ('Wyświetlanie treści\n',listmarketing)

# wstawienie 'investor relations' na pozycję nr 2
listmarketing.insert(2,'investor relations')

# skopiowanie zawartości listy listmarketing do emailMarketing
emailMarketing=listmarketing.copy()

# sortowanie listy emailMarketing

emailMarketing.sort()
print ("Posortowana zawartość 'emailMarketing'\n", emailMarketing)

# nowa lista jednoelementowa internalEmails
internalEmails =['internal communication']

# połączenie list emailMarketing i internalEmails
emailMarketing.extend(internalEmails)
print ("Elementy listy 'emailMarketing'", emailMarketing)

# utworzenie tuple 'emailMarketing'
print ('Utworzenie tuple')
emailMarketing=tuple(emailMarketing)

print (emailMarketing)


