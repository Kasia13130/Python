brandOnSale = "Opel"


class Car:
    """
    Car - class operating on cars available in the dealer
    """

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale):
        """
            init - arguments accepted:
            brand - the brand of the car ie Fiat
            model - the model of the car ie Multipla
            isAirBagOk - is the AirBag not used
            isPaintingOk - is the car paint original/no correction
            isMechanicOk - is the car fine or any mechanics failure
            isOnSale - is the car covered by extra promotion (some additional conditions apply)
        """
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        self.__isOnSale = isOnSale

    @property
    def IsOnSale(self):
        """IsOnSale - the car is on extra promotion that is limited in time (only selected cars may be "On Sale\""""
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

help(Car)
help(Car.IsOnSale)

new_car = Car