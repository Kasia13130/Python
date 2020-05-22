def DoAction(action, parameter):
    print("action:", action)
    print("parameter:", parameter)
    return


DoAction("buy", "shoes")

print("\n")

def DoAction2(action, *parameter):
    print("action:", action)
    print("parameter:", parameter)
    for element in parameter:
        print("element is", element)
    return


DoAction2("buy", "shoes", "socks")
DoAction2("buy", "shoes", "socks", "t-shirt")

print("\n")

def DoAction3(action, what, **parameter):
    print("action:", action)
    print("what:", what)
    print("parameter:", parameter)
    for element in parameter:
        print(element, "=", parameter[element])
    return


DoAction3("buy", "shoes", size=45, color="brown", type="sport")

print("\n")


# cwiczenie 1
def PrintAnimal(*animals):
    #print("animals", animals)

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

    for animal in animals:
        if animal == "cat":
            print("cat", "\t", txt_cat)
        elif animal == "bear":
            print("bear", "\t", txt_bear)
        elif animal == "bat":
            print("bat", "\t", txt_bat)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % (animal))
    return


PrintAnimal("cat", "bear", "bat")
PrintAnimal("cat", "bear", "bat", "elephant")


print('\n')


# cwiczenie 2
from datetime import date

def NewYearsEveDay(*dates):

    for date_today in dates:

        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print("Date: ", date_today, "How many days to end of year:", delta.days)

NewYearsEveDay(date(2020, 7, 4), date(2020, 5, 26), date(2020, 11, 14))
