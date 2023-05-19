def GIVEWORKINGDAY(year, month,day):
    # importowanie do pamięci funkcji date
    from datetime import date
    # importowanie do pamięci funkcji timedelta dla okręślenia różnicy dnia roboczego
    from datetime import timedelta

    #day = date.today()

    #day = date(2005,9,24)
    
    day = date(year,month,day)
    if day.weekday()==5:
        workingday = day + timedelta(days=2)
    elif day.weekday()==6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day
    print ('najbliższy dzień roboczy',day,'jest',workingday)

GIVEWORKINGDAY(2017,9,30)
GIVEWORKINGDAY(year=2017, month=9,day=9)
GIVEWORKINGDAY(month=12, day=9,year=2018)
