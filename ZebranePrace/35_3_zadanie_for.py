'''Dana jest lista:

    data = ['Error:File cannot be open',
            'Error:No free space on disk',
            'Error:File missing',
            'Warning:Internet connection lost',
            'Error:Access denied']

Zmieniamy zasady wyświetlania:

- Jeżeli w elements[0] znajduje się napis "Error",
wyświetl elements[1] konwertując tekst do wielkich liter

- w przeciwnym razie wyświetl elements[1] bez żadnej konwersji'''



data=['Error:File cannot be open','Error:No free space on disk','Error:File missing','Warning:Internet connection lost','Error:Access denied']

for elementy in data:
    elements = elementy.split(":")
    print (elements[0].upper())
    print (elements[1])
print ('|------------------|')

for elementy in data:
    elements = elementy.split(":")
    if elements[0].find('Error'):
        print(elements[1].upper())
    else:
        print (elements[1])
