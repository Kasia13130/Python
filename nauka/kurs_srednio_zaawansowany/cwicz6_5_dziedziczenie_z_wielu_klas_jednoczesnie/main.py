class Car:

    def __init__(self, brand, model, isOnSale):
        print(">> Class Car - init - starting")
        self.brand = brand
        self.model = model
        self.isOnSale = isOnSale
        self.name = "{} {}".format(brand, model)
        print(">> Class Car - init - finishing")

    def GetInfo(self):
        print(">> Class Car - GetInfo - starting")
        super().GetInfo()
        print("{} {}".format(self.brand, self.model).upper())
        print("IS ON SALE            {}".format(self.isOnSale))
        print(">> Class Car - GetInfo - stopping")


class Specialist:

    def __init__(self, firstname, lastname, brand):
        print(">> Class Specialist - init - starting")
        self.firstname = firstname
        self.lastname = lastname
        self.name = "{} {}".format(firstname, lastname)
        self.brand = brand
        print(">> Class Specialist - init - finishing")

    def GetInfo(self):
        print(">> Class Specialist - GetInfo - starting")
        print("{} {} - ({})".format(self.firstname, self.lastname, self.brand))
        print(">> Class Specialist - GetInfo - finishing")


class CarSpecialist(Car, Specialist):

    def __init__(self, brand, model, isOnSale, firstname, lastname):
        print(">> Class CarSpecialist - init - starting")
        Car.__init__(self, brand, model, isOnSale)
        Specialist.__init__(self, firstname, lastname, brand.upper())
        print(">> Class CarSpecialist - init - finishing")

    def GetInfo(self):
        print(">> Class CarSpecialist - GetInfo - starting")
        super().GetInfo()
        print(">> Class CarSpecialist - GetInfo - finishing")


tom = CarSpecialist("Toyota", "Corolla", True, "Tom", "Smith")
print(vars(tom))


tom.GetInfo()
print(CarSpecialist.__mro__)