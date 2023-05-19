import time

print (time.time())
print ('---Jako czas liczony od 01 stycznia 1970-----------\n')

print (time.localtime(time.time()))
print ('---Jako tupel-----------\n')

print (time.asctime(time.localtime(time.time())))
print ('---Jako czas odczytywlany przez człowieka-----------\n')

import calendar

print (calendar.month(2019,8,w=5,l=1))
print ('---z parametrem szerokości i wysokości-----------\n')

print (calendar.month(2019,8))
print ('---bez parametru-----------\n')

print ('Dzisiaj jest: ',calendar.weekday(2019,8,12))
print ('---Dzień tygodnia-----------\n')

print (calendar.isleap(2020))
print ('--- czy rok jest przestępny-----------\n')

print (calendar.leapdays(2000,2017))
print ('--- ile było dni przestpnych-----------\n')

print (calendar.calendar(2019))
