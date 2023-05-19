"""
Podstawowe sposoby otwierania plików
r - R ead (czytanie) - domyślne
w - W rite (pisanie) - jeśli plik istniał to go usunie,
                        jeśli nie to go stworzy
a - A ppend (dopisywanie)

mnogie tryby otwierania plików:
r+ - do czytania i pisania

w+ - do pisania i czytania
różnie się tym, że usunie zawartość istniejącego pliku
lub stworzy plik gduy go nie było

a+ - "wieczny tryb" dopisywania i czytania
UWAGA! Wskaźnik dopisywania jest zawsze na końcu
jeśli plik nie istniał - stworzy go

"""
with open("oceany.txt","a+", encoding="UTF-8") as file:
    file.write("Ocean Daniela")
