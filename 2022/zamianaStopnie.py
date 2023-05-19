'''Program, który zapyta użytkownika:
aby zamienić stopnie Celsjusza na Fahrenheit napisz 1, aby dokonać odwrotej zamiany
napisz 2,
a nastepnie zapytaj do o wartość zamiany'''
tC = 0
tF = 0
zamiana = input("Dokonaj wyboru, zamiana Celsjusza na Fahrenheita - wybierz 1, odwrotnie - wybierz 2: ")
if zamiana == '1':
    tC = int(input('Podaj wartość stopni Celcjusza: '))
    tF = 32+(9/5*tC)
    print(f'{tC} stopnia Celcjusza to {tF:.2f} stopnia Fahrenheita')
elif zamiana == '2':
    tF = int(input('Podaj wartość stopni Fahrenheita: '))
    tC = (5/9*(tF-32))
    print(f'{tF} stopnia Fahrenheita to {tC:.2F} stopnia Celcjusza ')
else:
    print(f'Nie podałeś właściwych danych')
    quit()
print('Koniec programu')