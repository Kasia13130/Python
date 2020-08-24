brandOnSale = "Opel"


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

    """def __GetIsOnSale(self):   """
    """    return self.__isOnSale """

    @property
    def IsOnSale(self):
        return self.__isOnSale

    @IsOnSale.setter
    def IsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print("Changing status IsOnSale to {} for {}".format(newIsOnSaleStatus, self.brand))
        else:
            print("Cannot change status IsOnSale. Sale valid only for {}".format(brandOnSale))

    @IsOnSale.deleter
    def IsOnSale(self):
        self.__isOnSale = None

    @property
    def CarTitle(self):
        return "Brand: {}, Model: {}".format(self.brand, self.model).title()


car_01 = Car("Seat", "Ibiza", True, True, True, False)

# print(car_01.IsOnSale())
print(car_01.IsOnSale)
car_01.IsOnSale = True
del car_01.IsOnSale
print(car_01.IsOnSale)
print(car_01.CarTitle)