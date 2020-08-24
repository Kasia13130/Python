'''
class Cake:

    known_types = ["cake", "cookies", "muffins", "other"]
    bakery_offer = []

    def __init__(self, name, kind, taste, additions, filling, weight, price, gluten_free, text):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = "other"
        self.taste = taste
        self.additions = additions
        self.filling = filling
        self.weight = weight
        self.price = price
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        self.__text = text
        if self.kind == "cake" or text == "":
            self.__text = text
        else:
            print("Error in: {}".format(name))

    def show_info(self):
        print("\n{}".format(self.name).upper())
        print("Kind: {}".format(self.kind))
        print("Taste: {}".format(self.taste))
        if self.additions != " ":
            print("Additives: ")
            for a in self.additions:
                print("\t{}".format(a))
        if self.filling != " ":
            print("Filling: {}".format(self.filling))

        if self.__gluten_free:
            print("Gluten free: {}".format("Yes"))
        else:
            print("Gluten free: {}".format("No"))

        if self.kind == "cake" or self.__text == "":
            print("Text on baking: {}".format(self.Text))
        else:
            print("Text on baking: {}".format("None"))

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additions.append(additives)

    def __get_text(self):
        print("Text on baking: {}".format("Happy Birthday:)"))      # wyswietlenie tekstu na ciescie po przez wlasciwosc
        # klasy
        return self.__text

    def __set_text(self, new_text):
        if self.__text == "cake" in self.kind:
            print("Status {} to {}".format(new_text, self.kind))

    Text = property(__get_text, __set_text, None, "Baking text")


cake_01 = Cake("Chocolate Cherry", "cake", "chocolate", ["sponge cake", "cherries", "icing"], "chocolate", 0.2, 9, False
, "Happy birthday")
cake_02 = Cake("Coconut", "cookies", "sweet", ["coconut", "cocoa topping"], " ", 0.05, 6.50, True, "")
cake_03 = Cake("Oranges", "muffins", "sweet-sour", ["pieces of orange"], "orange mus, cream filling", 0.3, 4, False, "")
cake_04 = Cake("Cocoa waffle", "waffle", "cocoa", [], "cocoa", 0.8, 4, False, "100 lat")

print("Today in our offer:")
for x in Cake.bakery_offer:
    x.show_info()
'''


class Cake:

    known_types = ["cake", "cookies", "muffins", "other"]
    bakery_offer = []

    def __init__(self, name, kind, taste, additions, filling, weight, price, gluten_free, text):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = "other"
        self.taste = taste
        self.additions = additions
        self.filling = filling
        self.weight = weight
        self.price = price
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        self.__text = text
        if self.kind == "cake" or text == "":
            self.__text = text
        else:
            print("Error in: {}".format(name))

    def show_info(self):
        print("\n{}".format(self.name).upper())
        print("Kind: {}".format(self.kind))
        print("Taste: {}".format(self.taste))

        if self.additions != " ":
            print("Additives: ")
            for a in self.additions:
                print("\t{}".format(a))

        if self.filling != " ":
            print("Filling: {}".format(self.filling))

        if self.__gluten_free:
            print("Gluten free: {}".format("Yes"))
        else:
            print("Gluten free: {}".format("No"))

        if self.kind == "cake" and self.__text != "":
            print("Text on baking: {}".format(self.__text))
        elif self.kind == "cake" and self.__text == "":     # wyswietlenie tylko tekstu z wlasciwosci Text
            print("".format(self.Text))

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additions.append(additives)

    def __get_text(self):
        print("Text on baking: {}".format("Happy Birthday:)"))      # wyswietlenie tekstu na ciescie po przez wlasciwosc
        # klasy
        return self.__text

    def __set_text(self, new_text):
        if self.__text == "cake" in self.kind:
            print("Status {} to {}".format(new_text, self.kind))

    Text = property(__get_text, __set_text, None, "Baking text")


cake_01 = Cake("Chocolate Cherry", "cake", "chocolate", ["sponge cake", "cherries", "icing"], "chocolate", 0.2, 9, False, "Happy birthday!!")
cake_02 = Cake("Coconut", "cookies", "sweet", ["coconut", "cocoa topping"], " ", 0.05, 6.50, True, "")
cake_03 = Cake("Oranges", "cake", "sweet-sour", ["pieces of orange"], "orange mus, cream filling", 0.3, 4, False, "Happy birthday :)")
cake_04 = Cake("Cocoa waffle", "waffle", "cocoa", [], "cocoa", 0.8, 4, False, "")

print("Today in our offer:")
for x in Cake.bakery_offer:
    x.show_info()


'''class Cake:

    known_types = ["cake", "cookies", "muffins", "other"]
    bakery_offer = []

    def __init__(self, name, kind, taste, additions, filling, weight, price, gluten_free, text):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = "other"
        self.taste = taste
        self.additions = additions
        self.filling = filling
        self.weight = weight
        self.price = price
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        self.__text = text
        if self.kind == "cake" or text == "":
            self.__text = text
        else:
            print("Error in: {}".format(name))

    def show_info(self):
        print("\n{}".format(self.name).upper())
        print("Kind: {}".format(self.kind))
        print("Taste: {}".format(self.taste))
        if self.additions != " ":
            print("Additives: ")
            for a in self.additions:
                print("\t{}".format(a))
        if self.filling != " ":
            print("Filling: {}".format(self.filling))

        if self.__gluten_free:
            print("Gluten free: {}".format("Yes"))
        else:
            print("Gluten free: {}".format("No"))

        if self.kind == "cake" or self.__text == "":
            print("Text on baking: {}".format(self.Text))       # wyswietlenie tekstu bez uzycia wlasciwosci Text
        else:
            print("Text on baking: {}".format("None"))

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additions.append(additives)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.__text == "cake" in self.kind:
            print("Status {} to {}".format(new_text, self.kind))

    Text = property(__get_text, __set_text, None, "Baking text")


cake_01 = Cake("Chocolate Cherry", "cake", "chocolate", ["sponge cake", "cherries", "icing"], "chocolate", 0.2, 9, False, "Happy birthday")
cake_02 = Cake("Coconut", "cookies", "sweet", ["coconut", "cocoa topping"], " ", 0.05, 6.50, True, "")
cake_03 = Cake("Oranges", "muffins", "sweet-sour", ["pieces of orange"], "orange mus, cream filling", 0.3, 4, False, "")
cake_04 = Cake("Cocoa waffle", "waffle", "cocoa", [], "cocoa", 0.8, 4, False, "100 lat")

print("Today in our offer:")
for x in Cake.bakery_offer:
    x.show_info()
'''

