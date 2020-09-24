class Car:

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, accessories):

        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        self.accessories = accessories

    def GetInfo(self):

        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag  - ok -       {}".format(self.isAirBagOk))
        print("Painting - ok -       {}".format(self.isPaintingOk))
        print("Mechanic - ok -       {}".format(self.isMechanicOk))
        print("Accessories           {}".format(self.accessories))
        print("----------------------------")

    def __iadd__(self, other):

        if type(other) is list:
            accessories = self.accessories
            accessories.extend(other)
            return Car(self.brand, self.model, self.isAirBagOk, self.isPaintingOk,
                       self.isMechanicOk, accessories)
        elif type(other) is str:
            accessories = self.accessories
            accessories.append(other)
            return Car(self.brand, self.model, self.isAirBagOk, self.isPaintingOk,
                       self.isMechanicOk, accessories)
        else:
            raise Exception("Adding type {} to Car is not implemented".format(type(other)))

    def __add__(self, other):

        if type(other) is Car:
            return [self, other]
        else:
            raise Exception("Adding type {} to Car is not implemented".format(type(other)))

    def __str__(self):
        return "Brand: {}, Model: {}".format(self.brand, self.model)


car_01 = Car("Seat", "Ibiza", True, True, True, ["winter tires"])
car_01.GetInfo()

car_01 +=["navigation system", "roof rack"]
car_01.GetInfo()

car_01 += "loudspeeker system"
car_01.GetInfo()

car_02 = Car("Opel", "Corsa", True, True, True, [])
car_pack = car_01 + car_02
print("car_01+car_02=", car_pack[0].brand, car_pack[1].brand)
print(car_pack)

print(car_01)
