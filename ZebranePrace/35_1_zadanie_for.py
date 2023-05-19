'''Dana jest lista:

    data = ['Error:File cannot be open',
            'Error:No free space on disk',
            'Error:File missing',
            'Warning:Internet connection lost',
            'Error:Access denied']

Napisz pętlę for, która wyświetli elementy tej listy jeden po drugim.
Podczas wyświetlania elementów konwertuj napisy do wielkich liter.'''

data=['Error:File cannot be open','Error:No free space on disk','Error:File missing','Warning:Internet connection lost','Error:Access denied']

for elementy in data:

    print (elementy.upper())
