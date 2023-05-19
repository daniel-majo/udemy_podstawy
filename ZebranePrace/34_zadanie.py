'''Poniższy program ma za zadanie (w nieco dziwny sposób!)
utworzyć napis o długości 10 znaków zapisany w zmiennej text.
Niestety coś poszło nie tak. Korzystając z debuggera znajdź przyczynę.
W odpowiedziach znajdziesz poprawną wersję skryptu z komentarzem'''


text = ''
number = 10
condition = True
     
while condition:
    text+='x'
    print(text)
    if len(text)>number:
        condition=False
