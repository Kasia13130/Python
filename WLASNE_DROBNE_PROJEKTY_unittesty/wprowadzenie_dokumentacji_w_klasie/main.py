class Cake:
    """
    Cake - class operating on bakery goods produced in a bakery
    """

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, weight, price):
        """
        init - arguments accepted:
        name - the name of the baking ie Rafaello
        kind - the kind of the baking ie cookies
        taste - describes the taste of the cake ie sweet
        additives - which is what's left added in the cake ie nuts
        filling - which what kind of the filling was added in cake
        weight - weight of a given baking
        price - price for the amount of a given baking
        """

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
        """ full_name - displays the name of the baked goods and its type"""
        return "{} --- {}\n".format(self.name.upper(), self.kind)


help(Cake)
help(Cake.full_name)
