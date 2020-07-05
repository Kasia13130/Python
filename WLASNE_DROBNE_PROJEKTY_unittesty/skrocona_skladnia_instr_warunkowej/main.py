# cwiczenie 1
price = 123
bonus = 23
bonus_granted = True


# postac uproszczona
prices = "price after bonus: {}".format(price - bonus) if bonus_granted else "No bonus awarded"
print(prices)
print("\n")


# cwiczenie 2
rating = 4

if rating == 5:
    pass
elif rating == 4:
    pass
else:
    pass

print("very good") if rating == 5 else print("good") if rating == 4 else print("weak")
print("\n")


# cwiczenie 3
import datetime
today_weekday = datetime.date.today().strftime("%A")

Weekday = "helping mom" if today_weekday == "Monday" else \
    "washing" if today_weekday == "Tuesday" or "Wednesday" else \
    "duty" if today_weekday == "Thursday" else \
    "two meetings" if today_weekday == "Friday" else \
    "lesson" if today_weekday == "Saturday" else "Sunady is ours"
print(Weekday)
print("\n")
