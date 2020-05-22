from datetime import date

def NewYearsEveDay(*dates):

    for date_today in dates:

        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print("Date: ", date_today, "How many days to end of year:", delta.days)

NewYearsEveDay(date(2020, 7, 4), date(2020, 5, 26), date(2020, 11, 14))