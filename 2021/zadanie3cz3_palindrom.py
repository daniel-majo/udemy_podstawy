'''
Przygotuj funkcję, która sprawdzi czy podany przez użytkownika wyraz jest palndromem.
Palindrom to wyraz lub wyrażenie czytane od lewej do prawej i odwrotnie wygląda tak samo
np. ala, sęka kęs, róg z gór
'''
def is_palindrom(word: str) -> bool:
    #wyrażenia bez spacji zapisane małymi literami
    #usuwanie spacji
    word = word.replace(' ', '')
    word = word.lower()
    return word[::-1] == word
    

print(is_palindrom('danielle k'))
print(is_palindrom('Sęka kęs'))
print(is_palindrom('ala'))
print(is_palindrom('róg z gór'))