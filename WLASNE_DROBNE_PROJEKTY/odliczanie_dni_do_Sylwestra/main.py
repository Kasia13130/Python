def NewYearsEveDay():
    # prints the new year's eve day
    from datetime import date

    date_today = date.today()
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today

    print(delta.days)
    return

NewYearsEveDay()