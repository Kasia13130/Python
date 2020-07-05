def NewYearsEveDay(year, month, day):
    # prints the new year's eve day
    from datetime import date

    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today

    print(delta.days)
    return


#NewYearsEveDay(2020, 6, 13)
#NewYearsEveDay(2020, 4, 25)
#NewYearsEveDay(2020, 2, 15)
#NewYearsEveDay(month=7, day=16, year=2020)