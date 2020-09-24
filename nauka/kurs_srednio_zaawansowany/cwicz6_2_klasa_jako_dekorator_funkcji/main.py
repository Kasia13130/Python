import random


class MemoryClass:

    list_of_already_selected_items = []

    def __init__(self, funct):
        print(">> this is init of MemoryClass")
        self.funct = funct

    def __call__(self, list):
        print(">> this is call of MemoryClass instance")
        items_not_selected = [i for i in list if i not in MemoryClass.list_of_already_selected_items]
        print("+-- selecting only from a list of", items_not_selected)
        item = self.funct(items_not_selected)
        MemoryClass.list_of_already_selected_items.append(item)
        return item


cars = ["Opel", "Toyota", "Fiat", "Ford", "Renault", "Mercedes", "BMW", "Peugeot", "Porsche", "Audi", "VW", "Mazda"]


@MemoryClass
def SelectTodayPromotion(list_of_cars):
    return random.choice(list_of_cars)


@MemoryClass
def SelectTodayShow(list_of_cars):
    return random.choice(list_of_cars)


@MemoryClass
def SelectFreeAccessories(list_of_cars):
    return random.choice(list_of_cars)


print("Promotion:", SelectTodayPromotion(cars))
print("Show:", SelectTodayShow(cars))
print("Free accessories:", SelectFreeAccessories(cars))

