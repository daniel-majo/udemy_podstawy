# '''
# listOfNumbers = [1,5,48,1,2]
# for numer in listOfNumbers:
#     print(numer)
# '''
'''
list = [1,2,3]
try:
    print(list[4])
except IndexError:# wykona się zamiast błędu
    print("Podałeś poza zakresem listy")
finally:# wykona się zawsze
    print("...")
    '''
# def mnozenie(liczba):
#     print(liczba*2)
# mnozenie(5)

'''
def poleKwadratu(a,b):
    a*b
    print(a*b)
poleKwadratu(4,5)
'''


wiek = input('Ile masz lat? ')
imie = input('Jak masz na imię ')
if wiek >= '18':
    print(f'Cześć, witam Cię Panie {imie}u. Masz {wiek} lat. Jesteś doroslły')
else:
    print(f'Cześć, witam Cię {imie}u. Masz {wiek} lat. Musisz troszkę poczekać')