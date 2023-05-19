def DNIDOSYLWKA(year, month, day):
    # importowanie do pamięci funkcji date
    from datetime import date

    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    
    delta = date_end_year - date_today

    print ('Do Sylwestra pozostało',delta.days,'dni')
    return
DNIDOSYLWKA(2019, 10, 6)
DNIDOSYLWKA(2019, 12, 23)
DNIDOSYLWKA(2020, 12, 23)

DNIDOSYLWKA(year=2021, month=12, day=21)
DNIDOSYLWKA(month=12, year=2021, day=21)
