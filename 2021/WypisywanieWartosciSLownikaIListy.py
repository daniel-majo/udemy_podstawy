people = {
    "ILSKDVLSLDVNLNLlklLNML":{'name':'John','age':15,'sex':'Male'},
    "alsfilastfkwasLlklLNML":{'name':'Martha','age':19,'sex':'Female'},
    "lamfolijsmauwxhmkaxdho":{'name':'Chiara','age':21,'sex':'Female'},
    "aloxkoaixdalwpxopPLOIP":{'name':'Andree','age':18,'sex':'Male'}
    }
'''
    [
    ("ILSKDVLSLDVNLNLlklLNML",{'name':'John','age':15,'sex':'Male'}),
    ("alsfilastfkwasLlklLNML",{'name':'Martha','age':19,'sex':'Female'}),
    ("lamfolijsmauwxhmkaxdho",{'name':'Chiara','age':21,'sex':'Female'}),
    ("aloxkoaixdalwpxopPLOIP",{'name':'Andree','age':18,'sex':'Male'})
    ]
    

pplist2 = [
            ('John', 27, 'Male'),
            ('John2', 25, 'Male'),
            ('John3', 28, 'Male')
         ]

for name, age, sex in pplist:
    print(name)
'''
for id, dictionary in people.items():   #wersja dla słownika we wnetrzu słownika
    print('ID -',id)
    for key in dictionary:
        print(key, '-',dictionary[key])
    
people2=[
        {'id':'laksflafljsfa4sfj','name':'Jan','age':'22','sex':'male'},
        {'id':'sdlsdglsdjljlmasf','name':'Janina','age':'26','sex':'female'},
        {'id':'qwfokeasmxlkasjlj','name':'Daniel','age':'32','sex':'male'}
    ]
oceny ={
    "Daniel":(3,5,2,6,4),
    "Elżbieta":(5,3,6,2,5,6,5)
    }


'''
print(people.items())


print(people["ILSKDVLSLDVNLNLlklLNML"])

print(people["ILSKDVLSLDVNLNLlklLNML"])

for dictionary in people:
    #print(people[dictionary])
    for sekDict in people[dictionary]:
        print(sekDict,people[dictionary][sekDict])
    




for key in people:
    print('ID:',key)
    for secendaryKeys in people[key]:
        print(secendaryKeys, people[key][secendaryKeys])




for dictionary in people2:
    for key in dictionary:
        print(key,'-',dictionary[key])

chcąc wypisać wartości kluczy ręcznie użyjemy poniższeo zapisu
print(oceny["Daniel"])
print(oceny["Elżbieta"])
print()


for key in oceny:
    ##print(oceny[key])
    print(key, "oceny" , oceny[key])

people1 = [
            "Daniel",
            "Elżbieta",
            "Zuzia",
            "Lidzia",
            "Pola"
          ]

for imie in people1:
    print(imie)

for dictionary in people2:
    for key in dictionary:
        print(key,'-', dictionary[key])
'''


