days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
workdays = days.copy()
workdays.remove("sat")
workdays.remove("sun")
print("All days: ", days)
print("Workdays: ", workdays)