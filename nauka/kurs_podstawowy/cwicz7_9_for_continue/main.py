'''
persons = ["Elizabeth", "Steven@sales.mycompany.com", "Sebastian", "Margareth", "Svetlana@mycompany.eu", "Raphael"]

domain = "mycompany.com"
emails = []

for person in persons:
    if "@" in person:
        emails.append(person)
    else:
        email = person + "@" + domain
        emails.append(email)

for email in emails:
    print(email)

print("\n")

persons = ["Elizabeth", "Steven@sales.mycompany.com", "Sebastian", "Margareth", "Svetlana@mycompany.eu", "Raphael"]

domain = "mycompany.com"
emails = []

for person in persons:
    if "@" in person:
        emails.append(person)
        continue
    email = person + "@" + domain
    emails.append(email)

for email in emails:
    print(email)

'''
print("\n")

# cwiczenie
menu = '''
Choose what want me to do for you:
1 - COFFEE
2 - TEA
3 - MAKE ME SMILE
---------------
To stop this script select 0
'''
smile = '''
 
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""""
'''

while True:
    print(menu)
    letter = input("Enter your choice ")

    if "1" == letter:
        print("Function COFFEE not implemented")
        input("Please press ENTER")
        continue
    if "2" == letter:
        print("Function TEA not implemented")
        input("Please press ENTER")
        continue
    if "3" == letter:
        print(smile)
        input("Please press ENTER")
        continue
    if "0" == letter:
        break

    input("You need to make a valid choice. Press ENTER and try again!")