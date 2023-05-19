import datetime

print ('Minimum i maximum year', datetime.MINYEAR, datetime.MAXYEAR)

# deltatime - wyliczanie różnicy czasu

d1=datetime.timedelta(days=1, hours=2, minutes=-30)
print (d1)

d2=datetime.timedelta(days=-1,hours=-2,minutes=-3)
print (d2)

print ('Timedelta sum:', d1+d2)


print ('Today is:', datetime.date.today())

today=datetime.date.today()
dayToPay=datetime.timedelta(days=7)

print ('Today is ',today)
print ('Bills should be paid within:',dayToPay)
print ('The bill should be paid till:', today+dayToPay)

bornDate=datetime.date(1979,2,19)
today=datetime.date.today()
print ('Przeżyłeś już ', today-bornDate,'dni')

# moduł datetime z elementem datetime-------------------------
print ('------------------------------------\n\n\n')
print ('now()\t',datetime.datetime.now())
print ('today()\t',datetime.datetime.today())
print ('utcnow()\t',datetime.datetime.utcnow())
print ('weekday()\t',datetime.datetime.today().weekday())

print ('------------------------------------\n\n\n')
print ('%a', datetime.datetime.now().strftime('%a'))
print ('%A', datetime.datetime.now().strftime('%A'))
print ('%w', datetime.datetime.now().strftime('%w'))
print ('%a %A %w', datetime.datetime.now().strftime('%a %A %w'))

print ('%Y-%m-%d_%H_%M_%S_%f', datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S_%f'))
