class Cake:

    def __init__(self, name, kind, taste, additions, filling, weight, price):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additions = additions
        self.filling = filling
        self.weight = weight
        self.price = price

    def show_info(self):
        print("\n{}".format(self.name).upper())
        print("Kind: {}".format(self.kind))
        print("Taste: {}".format(self.taste))
        if self.additions != " ":
            print("Additives: ")
            for x in self.additions:
                print("\t{}".format(x))
        if self.filling != " ":
            print("Filling: {}".format(self.filling))

    def set_filling(self):
        self.filling = "cream"

    def add_additives(self):
        self.additions.append("fruits")


cake_01 = Cake("Chocolate Cherry", "cake", "chocolate", ["sponge cake", "cherries", "icing"], "chocolate", 0.2, 9)
cake_02 = Cake("Coconut", "cookies", "sweet", ["coconut", "cocoa topping"], " ", 0.05, 6.50)
cake_03 = Cake("Oranges", "muffins", "sweet-sour", ["pieces of orange"], "orange mus, cream filling", 0.3, 4)

cake_01.set_filling()

cake_03.add_additives()

bakery_offer = []
bakery_offer.append(cake_01)
bakery_offer.append(cake_02)
bakery_offer.append(cake_03)

print("Today in our offer:")
for x in bakery_offer:
    x.show_info()