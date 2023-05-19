waga=int(input('Podaj swoja wagę np. 64 [kg]'))
wzrost=float(input('Podaj swoj wzrost np. 1.64 [m]'))

bmi=waga/(wzrost**2)
if (bmi<18.5):
    print ('Niedowaga')
elif (24>bmi>18.5):
    print ('Waga normalna')
elif (26.5>bmi>24):
    print ('Lekka nadwaga')
elif (30>bmi>26.5):
    print ('Nadwaga')
elif (35>bmi>30):
    print ('Otyłość I stopnia')
elif (40>bmi>30):
    print ('Otyłość II stopnia')
else:
    print ('Otyłość III stopnia')

