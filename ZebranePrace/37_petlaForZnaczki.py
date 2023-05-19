string_A='+---+---+---+---+'
string_B='|   |   |   |   |'

for znaczki in range(10):
    print (string_A)
print(25*"x")


for znaczki in range(9):
    if znaczki%2==0:
        print (string_A)
    else:
        print (string_B)

print(25*"x")

for i in range(10):
    print (i*'x')

print(25*"x")

for i in range(1,10):
    if i%2!=0:
        print(i*'o')
    else:
        print (i*'x')


