'''
Odbierz od użytkownika jego numer PESEL,
a nastepnie wiedząc, że dwa znaki możesz wyciąć za pomocą print(pesel[0:2] lub print(pesel[2:4)])
spróbuj zamienić go na datę urodzenia!
Pamiętaj o osobach urodzonych po 2000 roku!
'''
#93012278295
#02282362748

number_pesel = input('Podaj swój numer pesel: ')
year = number_pesel[0:2]
month = number_pesel[2:4]
day = number_pesel[4:6]
if month <= '12':
    print(f'Urodziłeś się w {day}-{month}-19{year} roku')
if month > '12':
    month_20 = int(month) - 20
    print(f'Urodziłeś się w {day}-{month_20}-20{year} roku')


