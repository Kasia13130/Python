
projects = ["Brexit", "Nord Stream", "US Mexico Border"]
leaders = ["Theresa May", "Wladimir Putin", "Donald Trump and Bill Clinton"]
for pro, lea in list(zip(projects, leaders)):
    print("The leader of '{}' is {}". format(pro, lea))


print("\n")
dates = ["2016-06-23", "2016-08-29", "1994-01-01"]
for pro, d, lea in list(zip(projects, dates, leaders)):
    print("The leader of '{}' started '{}' is {}". format(pro, d, lea))


print("\n")
for i, (pro, d, lea) in enumerate(zip(projects, dates, leaders)):
    print(i + 1, "- The leader of '{}' started '{}' is {}". format(pro, d, lea))
