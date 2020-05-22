def GiveWorkingDay(year, month, day):
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


GiveWorkingDay(2020, 3, 20)
GiveWorkingDay(2020, 4, 2)
GiveWorkingDay(2020, 4, 3)
GiveWorkingDay(2020, 4, 4)
GiveWorkingDay(2020, 4, 5)
GiveWorkingDay(2020, 4, 6)
GiveWorkingDay(2020, 4, 7)
GiveWorkingDay(day=5, month=6, year=2020)

print("\n")

# cwiczenie


def PrintAnimal(animal):

    if animal == "cat":
        txt = r'''
        |\---/|
        | o_o |
         \_^_/'''
        print(txt)
        return
    elif animal == "bear":
        txt = r'''
        /  \.-"""-./  \
        \    -   -    /
         |   o   o   |
         \  .-'"'-.  /
          '-\__Y__/-'
             `---`'''
        print(txt)
        return
    elif animal == "bat":
        txt = r'''
           /\                 /\
          / \'._   (\_/)   _.'/ \
         /_.''._'--('.')--'_.''._\
         | \_ / `;=/ " \=;` \ _/ |
          \/ `\__|`\___/`|__/`  \/
                  \(/|\)/  
             '''
        print(txt)
        return
    else:
        print("Canot print '%s'. Correct values for the parameter are: cat, bear, bat" % (animal))


PrintAnimal("cat")
PrintAnimal("bear")
PrintAnimal("bat")
PrintAnimal("cos")
PrintAnimal(animal="bear")

print("\n")

# inny zapis
def PrintAnimal(animal):
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


PrintAnimal('cat')
PrintAnimal(animal='bear')
PrintAnimal(animal='bat')
PrintAnimal('unicorn')

print("\n")


# cwiczenie 2
def NewYearsEveDay(year, month, day):
    # prints the new year's eve day
    from datetime import date

    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today

    print(delta.days)
    return


NewYearsEveDay(2020, 6, 13)
NewYearsEveDay(2020, 4, 25)
NewYearsEveDay(2020, 2, 15)
NewYearsEveDay(month=7, day=16, year=2020)