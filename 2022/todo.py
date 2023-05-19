'''
Dodajemy ważne rzeczy do zrobienia do bazy danych, a nstępnie możemy 
oznaczyć je jako zrobione

todos:                                              <--struktura bazy danych
id - int, primary key, autoinc
text - text
is_done - boolean

python todo.py --add "Wstaw ziemniaki"              <-- aby odpalić zadanie
python todo.py --list                               <-- aby wyświetlić listę zadań
python todo.py --toggle 1                           <-- aby ustawić zadanie zrobione

1. Zrób zakupy                  [ ]
2. Wstaw ziemniaki              [ ] 
3. Ugotuj rosół                 [ ]
4. Powieś pranie                [ ]
5.Umyj okna                     [ ]
6. Odrabianie lekcji            [v]
7. Nagrywanie filmów            [v]
'''
import sqlite3
from argparse import ArgumentParser

parser = ArgumentParser(description='Mała aplikacja TODO')
parser.add_argument('--install', help='UWAGA INSTALACJA! wyczyści bazę danych',action='store_true')
parser.add_argument('--add', help='Dodaj nowe zadanie')
parser.add_argument('--list', help='Wypisz tematy do zrobienia.', action='store_true')
parser.add_argument('--toggle', help='Zmień status zadania')
args = parser.parse_args()

connection = sqlite3.connect('todo.db')
cursor = connection.cursor()

if args.install:
    print('Instalujemy program.')
    cursor.execute('DROP TABLE todos')
    cursor.execute('CREATE TABLE todos(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, is_done BOOLEAN)')
    connection.commit()

if args.add is not None:
    print('Dodajemy...')
    title = args.add
    cursor.execute('INSERT INTO todos(title, is_done) VALUES(?, false)', (title,))# aby dodać nowy wpis
    connection.commit()
    
if args.toggle is not None:
    print('Przełączamy...')
    query = cursor.execute('SELECT is_done FROM todos WHERE id=?', (args.toggle,))
    is_done = query.fetchone()
    if is_done is None:
        print('Nie mam takiego TODO')
        quit()
    elif is_done[0] == 1:
        print('Zamieniam na niezrobione')
        new_is_done = 0
    elif is_done[0] == 0:
        print('Zamieniam na zrobione')
        new_is_done = 1
    
    cursor.execute('UPDATE todos SET is_done=? WHERE id=?', (new_is_done, args.toggle))
    connection.commit()

if args.list:
    for todo_id, title, is_done in cursor.execute('SELECT id, title, is_done FROM todos'):
        print(f'{todo_id} \t {title} \t {"[v]" if is_done else "[ ]"}')
    