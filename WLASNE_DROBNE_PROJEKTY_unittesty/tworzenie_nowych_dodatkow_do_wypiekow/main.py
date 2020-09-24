class Cake:

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

    def __str__(self):
        return "Name: {} \tKind: {} \tAdditives: {}".format(self.name.title(), self.kind,
                                                            self.additives)

    def __iadd__(self, other):

        if type(other) is str:
            self.additives.append(other)
            return Cake(self.name, self.kind, self.taste, self.additives, self.filling,
                        self.price, self.weight)

        elif type(other) is list:
            self.additives.extend(other)
            return Cake(self.name, self.kind, self.taste, self.additives, self.filling,
                        self.price, self.weight)

        else:
            print("Please enter list or string")


cake_01 = Cake("Chocolate Cherry", "cake", "chocolate", ["sponge cake", "cherries", "icing"], "chocolate", 0.2, 9)
cake_02 = Cake("Coconut", "cookies", "sweet", ["coconut", "cocoa topping"], " ", 0.05, 6.50)
cake_03 = Cake("Oranges", "cake", "sweet-sour", ["pieces of orange"], "orange mus, cream filling", 0.3, 4)
cake_04 = Cake("Cocoa waffle", "waffle", "cocoa", [], "cocoa", 0.8, 4)

cake_01 += "pieces of oranges"
cake_02 += ["sunflower seeds", "pieces of raspberries"]
cake_03 += 2


print(cake_01)
print(cake_02)
print(cake_03)
print(cake_04)
