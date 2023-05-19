"""
PLIK - nazwana lokacja, które przechowuje na STAŁE dane na dysku.
RAM - pomięć podręczna komputera, gdzie przechowywane są dane TYMCZASOWO
Operacje na plikach
1) otwieranie
2) pisanie/czytanie
3) zamykanie

Podstawowe sposoby otwierania plików
r - R ead (czytanie) - domyślne
w - W rite (pisanie) - jeśli plik istniał to go usunie,
                        jeśli nie to go stworzy
a - A ppend (dopisywanie)

tell - mówi, gdzie skończyliśmy ostatnią operację na pliku
seek - szuka(zmienia), na miejsce wskazane przez nas

"""
with open("oceany.txt","a", encoding="UTF-8") as file:
    file.write("\nPołudniowy")
