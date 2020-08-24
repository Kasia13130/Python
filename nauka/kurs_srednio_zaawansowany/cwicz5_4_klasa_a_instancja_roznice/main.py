
class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamage(self):
        return not (self.isAirBagOk, self.isPaintingOk, self.isMechanicOk)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag  - ok -       {}".format(self.isAirBagOk))
        print("Painting - ok -       {}".format(self.isPaintingOk))
        print("Mechanic - ok -       {}".format(self.isMechanicOk))
        print("----------------------------")


print("Class level variables BEFORE creating instances:", Car.numberOfCars, Car.listOfCars)

car_01 = Car("Seat", "Ibiza", True, True, True)
car_02 = Car("Opel", "Corsa", True, False, True)

print("Class level variables AFTER creating instances:", Car.numberOfCars, Car.listOfCars)

print("Id of class is:", id(Car))
print("Id of instances are:", id(car_01), id(car_02))

print("Check if object belongs to class:", isinstance(car_01, Car))
print("Check if object belongs using type:", type(car_01) is Car)
print("Check class of an object using __class__:", car_01.__class__)

print("List of instance attributes with values:", vars(car_01))
print("List of class attributes with values:", vars(Car))

print("List of instance attributes with values:", dir(car_01))
print("List of class attributes with values:", dir(Car))
#Car.numberOfCars = 123

print("Value taken from instance:", car_01.numberOfCars, "Value taken from class", Car.numberOfCars)
