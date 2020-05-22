from datetime import date
from datetime import timedelta

def GiveWorkingDay(year=date.today().year,
                   month=date.today().month,
                   day=date.today().day):
    # prints the nearest working day date
    day = date(year, month, day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    return workingday

nextworkingday = GiveWorkingDay(2017, 9, 2)
print("Next working day after", 2017, 9, 2, "is", nextworkingday)
nextworkingday = GiveWorkingDay()
print("Next working day after today is", nextworkingday)

print("Next working day after today is", GiveWorkingDay())

print("\n")


# cwiczenie
def PrintAnimal(animal=""):
    txt_cat = r'''
|\---/|
| o_o |
 \_^_/'''
    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    txt_bat = r'''
  /\                 /\
 / \'._   (\_/)   _.'/ \
/_.''._'--('.')--'_.''._\
| \_ / `;=/ " \=;` \ _/ |
 \/ `\__|`\___/`|__/`  \/
         \(/|\)/  
          '''
    if animal == "cat":
        print(txt_cat)
    elif animal == "bear":
        print(txt_bear)
    elif animal == "bat":
        print(txt_bat)
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % (animal))
        return False
    return True


if PrintAnimal():
    print("Parameter was correct")
else:
    print("Parameter was INCORRECT")

if PrintAnimal("bear"):
    print("Parameter was correct")
else:
    print("Parameter was INCORRECT")

if PrintAnimal("elephant"):
    print("Parameter was correct")
else:
    print("Parameter was INCORRECT")

nextanimal = PrintAnimal("cat")
print(nextanimal)
nextanimal = PrintAnimal("")
print(nextanimal)

print('\n')


# cwiczenie 2
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