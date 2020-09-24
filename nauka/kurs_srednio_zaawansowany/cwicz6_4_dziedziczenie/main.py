
brandOnSale = "Opel"


class Car(object):

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale):

        print(">> This is __init__ of parent class:", self.__class__.__name__)
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

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print("Changing status IsOnSale to {} for {}".format(newIsOnSaleStatus, self.brand))
        else:
            print("Cannot change status IsOnSale. Sale valid only for {}".format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, "if set to true, the car is available in sale/promo")


class Truck(Car):

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale, capacityKg):
        print(">> This is __init__ of child class:", self.__class__.__name__)
        super().__init__(brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale)
        self.capacityKg = capacityKg

    def GetInfo(self):
        super().GetInfo()
        print("CapacityKg   -   {}".format(self.capacityKg))


truck_01 = Truck("Ford", "Transit", True, False, True, False, 1600)
truck_02 = Truck("Renault", "Trafic", True, True, True, True, 1200)

print("Calling properties:")
print(truck_01.brand, truck_01.capacityKg, truck_01.IsOnSale, truck_02.brand,
      truck_02.capacityKg, truck_02.IsOnSale)

truck_01.GetInfo()
truck_02.GetInfo()
