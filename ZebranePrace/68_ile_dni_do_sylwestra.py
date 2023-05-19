def DNIDOSYLWKA():
    # importowanie do pamięci funkcji date
    from datetime import date

    date_today = date.today()
    current_year = date_today.year
    date_end_year = date(current_year,12,31)

    delta = date_end_year - date_today

    print ('Do Sylwestra pozostało',delta.days,'dni')
    return
DNIDOSYLWKA()
