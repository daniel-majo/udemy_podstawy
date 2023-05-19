'''
Wykładowca mówi studentom. Zaliczysz semestr jeżeli masz obecność
co najmniej 80% i średnią >= 3.0 lub zaliczyłeś pracę semestralną.
Zbuduj wyrażenie w Python które stwierdzi czy student, który ma obecność 0.85,
średnią 3.5 i nie zaliczył pracy semestralnej zda czy nie.
'''
##
##obecnosc = 0.4
##srednia = 2.5
##praca_semestralna = True
##
##zaliczenie = (obecnosc >=0.8 and srednia >=3.5 or praca_semestralna)
##print ("Zaliczyłeś semestr", zaliczenie)


obecnosc = 0.85
srednia =3.5
praca_zaliczeniowa = False
print (obecnosc, srednia, praca_zaliczeniowa)
print('Student ma obecność i ma średnią lub pracę zaliczeniową',obecnosc >=0.8 and srednia >=3 or praca_zaliczeniowa)
print('Student ma obecność i ma średnią i pracę zaliczeniową',obecnosc >=0.8 and srednia >=3 and praca_zaliczeniowa)
obecnosc = 0.4
srednia =2.5
praca_zaliczeniowa = True
print (obecnosc, srednia, praca_zaliczeniowa)
print('Student ma obecność i ma średnią lub pracę zaliczeniową',obecnosc >=0.8 and srednia >=3 or praca_zaliczeniowa)
print('Student ma obecność i ma średnią i pracę zaliczeniową',obecnosc >=0.8 and srednia >=3 and praca_zaliczeniowa)

##obecnosc = 0.8
##srednia = 3.5
##praca_semestralna = True
##if obecnosc>=0.8 and srednia>=3.0:
##    print ('Zaliczyl')
##elif praca_semestralna == True:
##    print ('Zaliczyl')
##else:
##    print ('Nie zaliczyl')
