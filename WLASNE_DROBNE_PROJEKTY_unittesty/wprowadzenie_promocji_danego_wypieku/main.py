from datetime import date
from datetime import timedelta


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

    @property
    def full_name(self):
        return "{} --- {}\n".format(self.name.upper(), self.kind)


class Promotion:

    def __init__(self, name, discount, start_date, end_date, minimal_order):

        self.name = name
        self.discount = discount
        self.start_date = start_date
        self.end_date = end_date
        self.minimal_order = minimal_order

    @property
    def full_name(self):
        return "Promotion {0:s} -- {1:.0%} -- from {2:} - to {3:} - about weight >= {4:} kg\n".format(self.name,
                                                                                                      self.discount,
                                                                                                      self.start_date,
                                                                                                      self.end_date,
                                                                                                      self.minimal_order)


cake1 = Cake("Chocolate Cherry", "cake", "chocolate", ["sponge cake", "cherries", "icing"], "chocolate", 0.2, 9)
cake1.show_info()

prom1 = Promotion("DISCUNT >> no additions <<", 0.20, date.today(), date.today() + timedelta(7), 0.5)
print(prom1.full_name)


class PromotionCake(Cake, Promotion):

    def __init__(self, cake1, prom1):
        Cake.__init__(self, cake1.name, cake1.kind, cake1.taste, cake1.additives, cake1.filling,
                      cake1.weight, cake1.price)
        Promotion.__init__(self, prom1.name, prom1.discount, prom1.start_date, prom1.end_date,
                           prom1.minimal_order)


prom_cake = PromotionCake(cake1, prom1)

prom_cake.show_info()

print(prom_cake.full_name)
print(PromotionCake.__mro__)


