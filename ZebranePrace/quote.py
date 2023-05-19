'''Cytat Doug Linder''' '''metody  na tekście'''
cytat='Dobry programista to człowiek, który spojrzy w obie strony zanim przejdzie przez jednokierunkową ulicę'
print (cytat)
print (cytat.capitalize()) # duża pierwsza litera
print (cytat.upper()) # zamiana na duże
print (cytat.lower())
print (cytat.endswith('ulicę'))
print (cytat.isupper())
print (cytat.upper().isupper())
print (cytat.find('jednokierunkową',0))
print (cytat.replace('jednokierunkową','1-kierunkową'))
print (cytat.replace('jednokierunkową','1-kierunkową').replace('obie','2'))
print (cytat.count('e'))
print (cytat.split(' '))
print (cytat.isdigit())
print (cytat.isdecimal())
print (cytat.isalpha())
print (cytat.isalnum())

