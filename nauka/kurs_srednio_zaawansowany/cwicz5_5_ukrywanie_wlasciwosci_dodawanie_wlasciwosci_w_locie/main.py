class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        self.__isOnSale = isOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamage(self):
        return not (self.isAirBagOk, self.isPaintingOk, self.isMechanicOk)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag  - ok -       {}".format(self.isAirBagOk))
        print("Painting - ok -       {}".format(self.isPaintingOk))
        print("Mechanic - ok -       {}".format(self.isMechanicOk))
        print("IS ON SALE            {}".format(self.__isOnSale))
        print("----------------------------")


car_01 = Car("Seat", "Ibiza", True, True, True, False)
car_02 = Car("Opel", "Corsa", True, False, True, True)

car_02.YearOfProduction = 2005
del car_02.YearOfProduction

setattr(car_02, "TAXI", False)
delattr(car_02, "TAXI")
print(hasattr(car_02, "TAXI"))

car_02.GetInfo()
print(vars(car_02))
