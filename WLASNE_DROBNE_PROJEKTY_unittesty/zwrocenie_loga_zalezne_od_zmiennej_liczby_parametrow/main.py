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