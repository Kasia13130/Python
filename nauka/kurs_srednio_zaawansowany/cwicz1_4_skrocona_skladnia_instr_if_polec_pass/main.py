dayType = 3

weekend = 1
workday = 2
holiday = 3

if dayType == 1:
    pass
elif dayType == 2:
    pass
else:
    pass

dayDescription = "weekend" if dayType == 1 else "?"
print(dayDescription)
print("\n")


dayDescription = "weekend" if dayType == 1 else "workday" if dayType == 2 else "holiday"
print(dayDescription)
print("\n")


print("weekend") if dayType == 1 else print("workday") if dayType == 2 else print("holiday")
