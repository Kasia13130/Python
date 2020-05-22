workDays = [19, 21, 22, 21, 20, 22]
months = ["I", "II", "III", "IV", "V", "VI"]

monthDays = dict(zip(months, workDays))
print(monthDays)

for key in monthDays:
    print("Key is", key, "value is", monthDays[key])

for value in monthDays.values():
    print("the value is", value)
