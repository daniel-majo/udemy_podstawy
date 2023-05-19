# ilość mrugnięć okiem na minutę

blinkPerMin=20 #ilość mrugnięć na minutę
minInHour=60   #ilość minut w godzinie
hourInDay=24   #ilość godzin na dobę
daysInYear=365 #ilość dni w roku
years=50       # ilość lat


#jezeli przyjac ze spimy 8 godzin to liczba godzin na dobe powinna wynosic 16
print(blinkPerMin*minInHour*(hourInDay - 8)*daysInYear*years)
