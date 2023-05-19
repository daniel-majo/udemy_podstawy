'''Odbierz od użtkownika imię i nazwisko, a następnie wiedząc,
że aby zamienić wszystkie litery na wielkie, wyświetl wyłącznie inicjały
np. 'Daniel' 'Majewski D.M.
'''
first_name = input('Podaj imię: ')
last_name = input('Podaj nazwisko: ')

#first_name_new = first_name.upper()
#last_name_new = last_name.upper()

print(f'{first_name.upper()[0]}.{last_name.upper()[0]}.')