from datetime import date
def NewYearsEveDay(year=date.today().year,
                   month=date.today().month,
                   day=date.today().day):
    # prints the new year's eve day
    from datetime import date

    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today

    return delta.days

print("Number of days until new year's eve: %d" % (NewYearsEveDay(2020, 8, 27)))
print("Number of days until new year's eve: %d" % (NewYearsEveDay(2020, 10, 17)))
print("Number of today days until new year's eve: %d" % (NewYearsEveDay()))