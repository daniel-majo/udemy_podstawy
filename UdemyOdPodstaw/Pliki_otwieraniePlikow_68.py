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

rozszerzenie to tylko 'tekst' nadawany po to, aby inne programy
        rozpoznawały plik w odpowiedni dla tych programów sposób

"""
a=5
file = open("test","w") # przechowanie to UCHWYT HANDLE
file.write("sample") # plik musi być zamknięty, aby wpisane dane były widoczne w pliku
file.close()
