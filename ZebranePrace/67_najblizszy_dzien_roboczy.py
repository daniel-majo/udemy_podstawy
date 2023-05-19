# importowanie do pamięci funkcji date
from datetime import date
# importowanie do pamięci funkcji timedelta dla okręślenia różnicy dnia roboczego
from datetime import timedelta

#day = date.today()

day = date(2005,9,24)

if day.weekday()==5:
    workingday = day + timedelta(days=2)
elif day.weekday()==6:
    workingday = day + timedelta(days=1)
else:
    workingday = day
print ('najbliższy dzień roboczy',day,'jest',workingday)
