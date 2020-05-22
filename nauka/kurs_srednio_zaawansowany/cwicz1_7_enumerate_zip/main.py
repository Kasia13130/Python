workDays = [19, 21, 22, 21, 20, 22]
print(workDays)

enumeratedDays = list(enumerate(workDays))
print(enumeratedDays)

for pos, value in enumeratedDays:
    print("position ", pos, "value", value)

months = ["I", "II", "III", "IV", "V", "VI"]
monthsDays = list(zip(months, workDays))
print(monthsDays)

for m, d in monthsDays:
    print("Month", m, "days", d)

for pos, (m, d) in enumerate(zip(months, workDays)):
    print("Position", pos, "month", m, "days", d)