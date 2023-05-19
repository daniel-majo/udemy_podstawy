import random

myNumbers=[]

while len(myNumbers) < 7:
    newNumbers=random.randint(1,49)
# w celu wyeliminowania dubletu    
    if newNumbers in myNumbers:
        print ('Dublet',newNumbers)
        continue
#------------------------
    myNumbers.append(newNumbers)
print ('Moje wylosowane liczby to: ',myNumbers)






