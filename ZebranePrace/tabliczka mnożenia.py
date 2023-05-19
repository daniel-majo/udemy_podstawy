# tabliczka mnożenia
'''szer=50
print ('-'*szer)
for a in range(1,6):
    for b in range(1,6):
        print(a,'x', b,'=', a*b)'''

# instrukcja if...elif...else
print ('Ile masz lat?')
lata=int(input('Podaj swoj wiek '))
if (lata>=18):
    liczba=100-lata
    print ('Jestes dorosłym człowiekiem')
    print ('Pozostało Ci ',liczba,'do 100 lat')
elif (lata>100):
    print ('Czy to naprawdę Twoj wiek?')
else:
    liczba=18-lata
    print ('Pozostało Ci',liczba,'lat do pełnoletnosci')