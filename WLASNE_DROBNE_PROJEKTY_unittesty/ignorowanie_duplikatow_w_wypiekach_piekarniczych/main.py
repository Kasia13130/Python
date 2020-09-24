class No_Duplicates:

    def __init__(self, funct):

        print("This is init")
        self.funct = funct

    def __call__(self, cake, additives):

        print("this is call")

        no_duplicate_list = []

        for i in additives:
            if i not in cake.additives:
                no_duplicate_list.append(i)
        self.funct(cake, no_duplicate_list)


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

        if self.filling != " ":
            print("Filling: {}".format(self.filling))

    def add_additives(self, additives):
        self.additives.extend(additives)


cake_01 = Cake("Chocolate Cherry", "cake", "chocolate", ["sponge cake", "cherries", "icing"], "chocolate", 0.2, 9)
cake_02 = Cake("Coconut", "cookies", "sweet", ["coconut", "cocoa topping"], " ", 0.05, 6.50)
cake_03 = Cake("Oranges", "cake", "sweet-sour", ["pieces of orange"], "orange mus, cream filling", 0.3, 4)
cake_04 = Cake("Cocoa waffle", "waffle", "cocoa", [], "cocoa", 0.8, 4)


@No_Duplicates
def add_extra_additives(cake, additives):
    cake.add_additives(additives)


add_extra_additives(cake_01, ["strawberries", "sugar-flowers"])
cake_01.show_info()

add_extra_additives(cake_01, ["strawberries", "sugar-flowers", "chocolade", "nuts"])
cake_01.show_info()
