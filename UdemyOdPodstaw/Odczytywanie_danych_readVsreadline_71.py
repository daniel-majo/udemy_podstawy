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
read
readline - czytanie pojedynczej linii
readlines - czytanie całości i wrzutka w listę z \n

splitlines - metoda usuwająca \n w pliku
file.encoding -sprawdzanie kodowania znaków

"""
with open("oceany.txt","r", encoding="UTF-8") as file:
    oceany=file.read().splitlines()
