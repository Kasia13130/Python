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