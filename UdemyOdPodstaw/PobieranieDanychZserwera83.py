'''
JSONplaceholder - miejsce zastępcze na two przyszły json

Popbieranie anych z serwera i odczytywanie danych
'''
# import requests
# import json


# r = requests.get("https://jsonplaceholder.typicode.com/todos")
# #tasks = json.loads(r.text)
# tasks = r.json()

# try:
#     tasks = r.json()
# except json.decoder.JSONDecodeError:
#     print("Niepoprawny format")
# else:
#     print("Wszystko OK")
#     print(tasks[0])
a = int(input("Podaj a "))
b = int(input("Podaj b "))
c = int(input("Podaj c "))
if a < b:
    if a < c:
        najmniejsza = a
    else:
        najmniejsza = c
else:
    if b < c:
        najmniejsza = b
    else:
        najmniejsza = c
print("Najmniejszą liczbą jest ", najmniejsza)

