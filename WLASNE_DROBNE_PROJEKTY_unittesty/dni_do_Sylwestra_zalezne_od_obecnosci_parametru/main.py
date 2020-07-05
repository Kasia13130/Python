from datetime import date


def NewYearsEveDay(year=date.today().year,
                   month=date.today().month,
                   day=date.today().day):
    # prints the new year's eve day

    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today

    print('Counting from ', date_today, 'days remaining', delta.days)
    return


'''NewYearsEveDay(2020, 6)
NewYearsEveDay(year=2020)
NewYearsEveDay(month=3)
NewYearsEveDay(month=7, year=2020)
NewYearsEveDay(day=25)
NewYearsEveDay(day=16, month=5, year=2022)'''