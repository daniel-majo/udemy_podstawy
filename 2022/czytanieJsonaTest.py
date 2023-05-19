'''
Ładujemy pytania z pliku json, a nstępnie wyświetla nam się quiz.
Odpowiadamy na przygotowane przez nas pytania... i dowaidujemy się ile zdobyliśmy punktów
'''
from json import load
correct_answer = 0

with open('quiz.json', encoding='utf8') as questions_file:
    questions = load(questions_file)

    for question in questions:
        print(question['question'])
        for index, answer in enumerate(question['answers']):
            print(index, answer['text'])

        user_answer = int(input("Jak myślisz, która odpowiedź jest prawidłowa? "))
        try:
            is_correct_answer = question['answers'][user_answer]['correct']
            if is_correct_answer:
                correct_answer += 1
        except IndexError:
            pass
                
        print(50*'-')
print('Uzyskałeś punktów', correct_answer)