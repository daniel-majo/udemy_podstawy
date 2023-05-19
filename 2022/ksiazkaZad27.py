'''
Napisz program, który pobierze liczbę sekund od użytkownika i jeśli użytkownik podał liczbę mniejszą niż 10,
zatrzyma się na tak długo, jaką liczbę użytkownik podał. Jęlsi podana liczba jest większa lub równa 20, to program poinformuje, że
nie będzie tyle czekać
'''
import time
wait = int(input('Jak długo mam czekać: '))
if wait < 10:
    time.sleep(wait)
else:
    print('Nie będę tyle czakać')
