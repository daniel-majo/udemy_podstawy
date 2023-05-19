'''
Przygotuj słownik posiadający 10 wyrazów napisanych
po polsku jako klucze oraz 10 wyrazów napisanych po angielsku jako wartości.

Zapytaj użytkownika o 5 losowych wyrazów, a następnie policz jaki procent odpowiedzi był
prawidłowy
'''
from random import shuffle
questions = {
    'mama':'mother',
    'tata':'father',
    'jabłko':'apple',
    'noga':'leg',
    'ręka':'hand',
    'samolot':'aeroplan',
    'kuchnia':'kitchen',
    'piłka nożna':'football',
    'komputer':'computer',
    'las':'forest'
}

polish_words = list(questions.keys()) #przerobienie ze słownika na listę
shuffle(polish_words)
# print(polish_words)

correct_answers = 0

for polish_word in polish_words[:5]:
    # print(polish_word)
    answer = input(f'Jak po angielsku będzie {polish_word} ? ')
    if answer == questions[polish_word]:
        correct_answers +=1
        print(correct_answers)
    else:
        print('Skup się...')

percent = correct_answers/5*100
print(f'Udzieliłeś {correct_answers} prawidłowych odpowiedzi, co stanowi {percent:.2f} %')