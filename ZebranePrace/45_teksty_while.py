'''
Dany jest tekst:

United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.

policz ile jest w nim słów dłuższych od wordLength = 6

Wskazówka:

-jako słowo potraktujemy każdy ciąg znaków rozdzielony spacją

-aby tekst podzielić na słowa skorzystaj z funkcji split(' ')
i zapisz wynik w liście listOfWords

-zadeklaruj zmienne shortWords i longWords=0

-pętlą przejdź przez listę słów i poleceniem IF badaj
czy napis jest służszy od wordLength. Jeśli tak zwiększ liczbę longWords o 1,
a jeśli nie to zwiększ shortWords

'''

word = 'United Space Alliance: This company provides major support to NASA for various projects, such as the space shuttle. One of its projects is to create Workflow Automation System (WAS), an application designed to manage NASA and other third-party projects. The setup uses a central Oracle database as a repository for information. Python was chosen over languages such as Java and C++ because it provides dynamic typing and pseudo-code–like syntax and it has an interpreter. The result is that the application is developed faster, and unit testing each piece is easier.'

wordLength = 6
listOfWords = word.split(' ')
#print (listOfWords)
#print (len(listOfWords))
shortWords = 0
longWords = 0
i=0
while i < len(listOfWords):
    if len(listOfWords[i]) > wordLength:
        longWords += 1
    else:
        shortWords += 1
    i+=1
print ('Liczba słów krótsza niż 6 znaków to: ', shortWords)
print ('Liczba słów dłuższa niż 6 znaków to: ', longWords)

