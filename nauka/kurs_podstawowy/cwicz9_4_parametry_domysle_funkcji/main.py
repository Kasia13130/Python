def GiveWorkingDay(year, month=1, day=1):
    # prints the nearest working day
    from datetime import date
    from datetime import timedelta

    day = date(year, month, day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print("working day for", day, "is", workingday)
    return


GiveWorkingDay(2020, 9)
GiveWorkingDay(2020, 9, 5)
GiveWorkingDay(2020)

print("\n")

from datetime import date
from datetime import timedelta


def GiveWorkingDay(year=date.today().year,
                   month=date.today().month,
                   day=date.today().day):
    # prints the nearest working day

    day = date(year, month, day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print("working day for", day, "is", workingday)
    return


GiveWorkingDay(2020, 9, 2)
GiveWorkingDay()
GiveWorkingDay(2020, 2)

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
        print("Canot print '%s'. Correct values for the parameter are: cat, bear, bat" % (animal))
    return


PrintAnimal("")
PrintAnimal("")
PrintAnimal(animal="cat")

print("\n")


def PrintAnimal(animal=''):
    # this function prints a cat, bear or bat ascii-art
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

    if animal == 'cat':
        print(txt_cat)
    elif animal == 'bear':
        print(txt_bear)
    elif animal == 'bat':
        print(txt_bat)
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)

    return
print("\n")


# cwiczenie 2
from datetime import date

def NewYearsEveDay(year=date.today().year,
                   month=date.today().month,
                   day=date.today().day):
    # prints the new year's eve day

    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today

    print('Counting from ', date_today,'days remaining', delta.days)
    return


NewYearsEveDay(2020, 6)
NewYearsEveDay(year=2020)
NewYearsEveDay(month=2)
NewYearsEveDay(month=7, year=2020)
NewYearsEveDay(day=25)
NewYearsEveDay(day=16, month=5, year=2022)