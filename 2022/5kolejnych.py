from dataclasses import dataclass
print ("NWD odejmowaniem")
a = int(input("Podaj a "))
b = int(input("Podaj b "))

while (a!=b):

    if (a>b):
        a = a - b
    else:
        b = b - a
print("NWD liczb jest", a)
input("\n aby zakończyć Enter")
    
    
    
