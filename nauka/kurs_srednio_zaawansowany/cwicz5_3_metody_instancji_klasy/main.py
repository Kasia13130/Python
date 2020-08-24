class Car:

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk

    def IsDamage(self):
        return not (self.isAirBagOk, self.isPaintingOk, self.isMechanicOk)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag  - ok -       {}".format(self.isAirBagOk))
        print("Painting - ok -       {}".format(self.isPaintingOk))
        print("Mechanic - ok -       {}".format(self.isMechanicOk))
        print("----------------------------")


car_01 = Car("Seat", "Ibiza", True, True, True)
car_02 = Car("Opel", "Corsa", True, False, True)

car_01.GetInfo()
car_02.GetInfo()


print(car_01.brand, car_01.model, car_01.IsDamage())
print(car_02.brand, car_02.model, car_02.IsDamage())

print(car_01.brand, car_01.model, car_01.isAirBagOk, car_01.isPaintingOk, car_01.isMechanicOk)
print(car_02.brand, car_02.model, car_02.isAirBagOk, car_02.isPaintingOk, car_02.isMechanicOk)
