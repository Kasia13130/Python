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