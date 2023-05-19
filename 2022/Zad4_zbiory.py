'''
Odbierz od użytkownika trzy wyrazy, a następnie znajdź wszystkie wspólne dla nich znaki.
np. 'abc','bcd','baq' powinno zwrócić set('b')

# print('Suma zbiorów', team_a | team_b) # pojedyńczy pajp, czyli |
# print('Częśc wspólna', team_a & team_b) # pojedyńczy ampersant &
# print('Różnica symetryczna', team_a ^ team_b) # pojedyńcza karetka ^
'''
word1 = set(input('Podaj słowo:'))
word2 = set(input('Podaj słowo:'))

print(word1 & word2)