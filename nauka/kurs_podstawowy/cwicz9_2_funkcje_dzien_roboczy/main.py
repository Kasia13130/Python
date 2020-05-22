def GiveWorkingDay():
    # prints the nearest working day
    from datetime import date
    from datetime import timedelta

    #day = date.today()
    day = date(2017,9,30)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print("working day for", day, "is", workingday)
    return

GiveWorkingDay()
GiveWorkingDay()

print("\n")
# cwiczenie
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