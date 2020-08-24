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

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print("Changing status IsOnSale to {} for {}".format(newIsOnSaleStatus, self.brand))
        else:
            print("Cannot change status IsOnSale. Sale valid only for {}".format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, "if set to true, the car is available in sale/promo")

    @classmethod
    def ReadFromText(cls, aText):
        aNewCar = cls(*aText.split(":"))
        return aNewCar

    @staticmethod
    def Convert_KM_KW(KM):
        return KM * 0.735

    @staticmethod
    def Convert_KW_KM(KW):
        return KW * 1.36


lineOfText = "Renault:Megane:True:True:False:False"

car_03 = Car.ReadFromText(lineOfText)
car_03.GetInfo()

print("converting 120 KM to KW", Car.Convert_KM_KW(120))
print("converting  90 KW to KM", Car.Convert_KW_KM(90))

# print(Car.GetInfo())
print(car_03.ReadFromText(lineOfText))
print(car_03.Convert_KW_KM(50))