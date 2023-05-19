'''Dana jest lista:

    data = ['Error:File cannot be open',
            'Error:No free space on disk',
            'Error:File missing',
            'Warning:Internet connection lost',
            'Error:Access denied']

Jak widzisz, każdy z elementów listy zawiera znak ":".

- W pętli for każdy z przetwarzanych napisów rozbij ze względu na ":"
korzystając z funkcji split.
- Wynik zapamiętaj w nowej dwuelementowej liście elements.
- Następnie wyświetl elements[0] konwertując napis do wielkich liter,
a elements[1] wyświetl bez żadnej konwersji'''



data=['Error:File cannot be open','Error:No free space on disk','Error:File missing','Warning:Internet connection lost','Error:Access denied']

for elementy in data:
    elements = elementy.split(":")
    print (elements[0].upper())
    print (elements[1])
