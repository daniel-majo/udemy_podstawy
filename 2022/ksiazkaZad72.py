'''
Napisz program, który sprawdza, czy tablica jest posortowana, czy nie. Jeśli tablica nie jest posortowana,
to pyta czy posortować.
# Tablica jest nieposrtowana. Czy chcesz ją posortować?
#Tak
#Posortowano
#['Asia', 'Janek', 'Staś', 'Kasia', 'Roman']
'''
first_name = ['Asia', 'Zosia', 'Staś', 'Kasia', 'Roman']
if first_name != first_name.sort():
    print('Tablica jest nieposortowana. Czy chcesz ją posortować?')
    if str(input(' ')) == 'Tak':
        first_name.sort()
        print(first_name)
