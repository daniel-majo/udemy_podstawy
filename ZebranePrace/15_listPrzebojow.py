# tworzenie listy piosenek
hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']

# dodawanie dwóch elementów do listy
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')

# wstawianie utworu 'HOTEL CALIFORNIA' na 3 pozycji
hitsTitles.insert(2,'HOTEL CALIFORNIA')

# wstawianie utworu 'THE SOUND OF SILENCE' na 1 pozycji
hitsTitles.insert(0,'THE SOUND OF SILENCE')

# wyszykiwanie indexu/ numeru pozycji dla utworu 'HOTEL CALIFORNIA'
print (hitsTitles.index('HOTEL CALIFORNIA'))

# usuwanie utworu 'HOTEL CALIFORNIA' z listy
hitsTitles.remove('HOTEL CALIFORNIA')

# zamiana elementu na licie
hitsTitles[0]=('ENJOY THE SILENCE')

# tworzenie kopii listy
hitsToRead = hitsTitles.copy()
print ('Kopia listy:', hitsToRead)

# nowa lista hitsToRead ma być w kolejności odwrotnej
hitsToRead.reverse()
print ('Kolejność odrotna:', hitsToRead)

# nowa lista hitsToRead ma być w kolejności alfabetycznej
hitsToRead.sort()
print ('Kolejność alfabetyczna:', hitsToRead)

# utworzenie kolejnej listy additionalSongs
additionalSongs=['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']

# dodanie listy additionalSongs do hitsToRead
hitsToRead.extend(additionalSongs)
print ('Po połączeniu dwóch list:', hitsToRead)

# ile razy występuje utwór 'WISH YOU WERE HERE' hitsToRead
hitsToRead.extend(additionalSongs)
print ('Ile razy występuje utwór "WISH YOU WERE HERE"\n',hitsToRead.count('WISH YOU WERE HERE'))

# ile razy występuje utwór 'RIDERS ON THE STORM' hitsToRead
hitsToRead.extend(additionalSongs)
print ('Ile razy występuje utwór "RIDERS ON THE STORM"\n',hitsToRead.count('RIDERS ON THE STORM'))

print ('Po połączeniu dwóch list:\n', hitsToRead)

# wyczyszczenie elementów list hitsToRead
hitsToRead.clear()

print ('Po zakończeniu list:\n', hitsToRead)

print (hitsTitles)

