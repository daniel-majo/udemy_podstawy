try:
    file = open("test","w") # przechowanie to UCHWYT-HANDLE
    file.write("sample") # plik musi być zamknięty, aby wpisane dane były widoczne w pliku
    print(0/0)
    file.write("sample")
finally:
    file.close()
