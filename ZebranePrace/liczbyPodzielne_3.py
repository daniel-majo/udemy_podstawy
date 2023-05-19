##a = int(input("Podaj lewy przedział: "))
##b = int(input("Podaj prawy przedział: "))
##
##x = a
##while x <= b:
##    if x%3 == 0:
##        print(x)
##    x = x + 1


a = int(input("Podaj lewy przedział: "))
b = int(input("Podaj prawy przedział: "))

x = a

while x%3 != 0:
    x = x + 1
while x <=b:
    print(x)
    x = x + 3
