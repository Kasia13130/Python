'''
def DisplayOptions(options):

    for i in range(len(options)):
        print("{} - {}".format(1 + i, options[i]))

    choice = input("Select option above or press enter to exit: ")

    return choice

options = ["load data", "export data", "analyze & predict"]
choice = "x"

while choice != "":
    choice = DisplayOptions(options)
    if choice != "":
        try:
            choice_num = int(choice)

            if choice_num == 1 or choice_num == 2 or choice_num == 3:

                if choice_num >= 0 and choice_num <= len(options):
                    print("Choice value: ", choice_num)

                else:
                    print("The choice is not correct. Please try again.")
            else:
                print("Please enter value integer.")
        except:
            print("Something went wrong.")
    else:
        print("Process is finished.")

DisplayOptions(options)
'''


def DisplayOptions(options):

    for i in range(len(options)):
        print("{} - {}".format(1 + i, options[i]))

    choice = input("Select option above or press enter to exit: ")

    return choice

options = ["load data", "export data", "analyze & predict"]
choice = "x"

while choice != "":
    choice = DisplayOptions(options)
    if choice != "":
        try:
            choice_num = int(choice)

            if choice_num == 1 or choice_num == 2 or choice_num == 3:

                if choice_num >= 0 and choice_num <= len(options):

                    if choice_num == 1:     # zostalo dodane
                        print("Choice information: ", choice_num, "-", options[0])
                    elif choice_num == 2:     # zostalo dodane
                        print("Choice information: ", choice_num, "-", options[1])
                    elif choice_num == 3:     # zostalo dodane
                        print("Choice information: ", choice_num, "-", options[2])
                else:
                    print("The choice is not correct. Please try again.")
            else:
                print("Please enter value integer.")
        except:
            print("Something went wrong.")
    else:
        print("Process is finished.")

DisplayOptions(options)