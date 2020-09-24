class Cake(object):

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, weight, price):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.weight = weight
        self.price = price
        self.bakery_offer.append(self)

    def show_info(self):
        print("\n{}".format(self.name.upper()))
        print("Kind: {}".format(self.kind))
        print("Taste: {}".format(self.taste))
        print("Additives: ")
        if self.additives != " ":
            for a in self.additives:
                print("\t\t{}".format(a))
        elif self.additives == "":
            print("No additives")

        if self.filling != "":
            print("Filling: {}".format(self.filling))

        print("Price: {} zl".format(self.price))
        print("Weight: {} kg".format(self.weight))

    @property
    def full_name(self):
        return "{} --- {}".format(self.name.upper(), self.kind)


cake_01 = Cake("Chocolate Cherry", "cake", "chocolate", ["sponge cake", "cherries", "icing"], "chocolate", 0.2, 9)
cake_02 = Cake("Coconut", "cookies", "sweet", ["coconut", "cocoa topping"], " ", 0.05, 6.50)
cake_03 = Cake("Oranges", "cake", "sweet-sour", ["pieces of orange"], "orange mus, cream filling", 0.3, 4)
cake_04 = Cake("Cocoa waffle", "waffle", "cocoa", [], "cocoa", 0.8, 4)


class SpecialCake(Cake):

    def __init__(self, name, kind, taste, additives, filling, weight, price, occesion, shape, ornaments, text):

        super().__init__(name, kind, taste, additives, filling, weight, price)
        self.occesion = occesion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text

    def show_info(self):
        super().show_info()
        print("Cake on:             {}".format(self.occesion))
        print("Shape of cake:       {}".format(self.shape))
        print("Ornaments on cake:   {}".format(self.ornaments))
        print("Text on cake:        {}".format(self.text))


birthday = SpecialCake("Chocolate cats", "cake", "chocolate", ["sponge cake", "cherries", "icing"], "chocolate", 0.2, 9, "birthday", "square", "cats", "100 years !!!")
wedding = SpecialCake("Rafaello", "cake", "sweet", ["sponge cake", "Coconut cream", "almonds"], "white chocolate", 0.5, 7, "wedding", "circle", "figurines", "Anne and Max")

birthday.show_info()
wedding.show_info()

for x in SpecialCake.bakery_offer:
    x.show_info()
    print(x.full_name)
