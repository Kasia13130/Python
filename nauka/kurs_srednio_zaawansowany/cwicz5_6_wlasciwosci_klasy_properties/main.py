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


car_01 = Car("Seat", "Ibiza", True, True, True, False)
car_02 = Car("Opel", "Corsa", True, False, True, True)

'''
print("Status of cars: ", car_01.__GetIsOnSale(), car_02.__GetIsOnSale())            
#print("Status of cars: ", car_01._Car__GetIsOnSale(), car_02._Car__GetIsOnSale())      
car_01.SetIsOnSale(True)
car_02.SetIsOnSale(False)
print("Status of cars: ", car_01.GetIsOnSale(), car_02.GetIsOnSale())

'''
car_01.IsOnSale = True
car_02.IsOnSale = True
print("Status of cars: ", car_01.IsOnSale, car_02.IsOnSale)


"""
# po przez wlasciwosc mozna ukryc pewne atrybuty i funkcje zamiast stosowac podkreslenia z nazwa klasy
brandOnSale = "Opel"       # mozliwosc modyfikowania sprzedazy tylko dla marki Opel


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
    

    def GetIsOnSale(self):         
        return self.__isOnSale        
           

    # def SetIsOnSale(self, newIsOnSaleStatus):
    def SetIsOnSale(self, newIsOnSaleStatus):   
        if self.brand == brandOnSale:           
            self.__isOnSale = newIsOnSaleStatus
            print("Changing status IsOnSale to {} for {}".format(newIsOnSaleStatus, self.brand))
        else:           
            print("Cannot change status IsOnSale. Sale valid only for {}".format(brandOnSale))   

    IsOnSale = property(GetIsOnSale, SetIsOnSale, None, "if set to true, the car is available in sale/promo")
    

car_01 = Car("Seat", "Ibiza", True, True, True, False)
car_02 = Car("Opel", "Corsa", True, False, True, True)

print("Status of cars: ", car_01.GetIsOnSale(), car_02.GetIsOnSale())            
#print("Status of cars: ", car_01.GetIsOnSale(), car_02.GetIsOnSale())
car_01.SetIsOnSale(True)
car_02.SetIsOnSale(False)
print("Status of cars: ", car_01.GetIsOnSale(), car_02.GetIsOnSale())


car_01.IsOnSale = True        
car_02.IsOnSale = True
print("Status of cars: ", car_01.IsOnSale, car_02.IsOnSale)      
"""