'''Gdzie otworzyć plik, co zrobić i zamknąć plik
'''

with file = open("test","w") as file: #UCHWYT HANDLE
    file.write("sample") 
    a=5
    file.write("sample")
