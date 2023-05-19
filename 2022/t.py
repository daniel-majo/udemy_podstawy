'''
i = 0
a = []
while > 2:
    #for i in range(5):
    a.append(input("Podaj dane do wprowadzenia do listy "))
    i += 1
print(a)
'''
def prostokat(a,b):
    return a*b

def kwadrat(a):
    return a*a

def trojkat(a,h):
    return 0.5*a*h

def trapez(a,b,h):
    return ((a+b)*h)/2

def kolo(r):
    return 3.14*r**2

wybor = input("Podaj swój wybór ")
if wybor == "1":
    print("Twój wybór to prostokąt")
    a = int(input("Podaj a "))
    b = int(input("Podaj b "))
    print(prostokat(a,b))
elif wybor =="2":
    print("Twój wybór to kwadrat")
    a = int(input("Podaj a "))
    print(kwadrat(a))
else:
    print("Koniec")
    
    




'''
1) prostokąta

2) kwadratu

3) trójkąta

4) trapezu

5) koła'''
    
