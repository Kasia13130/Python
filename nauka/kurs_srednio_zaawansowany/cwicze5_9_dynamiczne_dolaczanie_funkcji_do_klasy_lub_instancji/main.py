"""import csv
import types


def exportToFile_Static(path, header, data):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
    print("Information was exported to file - static method")


def exportToFile_Class(cls, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["brand", "model", "IsOnSale"])
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])
    print("Information was exported to file - class method")


def exportToFile_Instance(self, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["brand", "model", "IsOnSale"])
        writer.writerow([self.brand, self.model, self.IsOnSale])
    print("Information was exported to file - instance method")


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

print("Static -----" * 5)
Car.ExportToFile_Static = exportToFile_Static
Car.ExportToFile_Static(r"/media/sf_phyton_nauka/kurs udemy/srednio_zaawansowany/cwicze5_9_dynamiczne_dolaczanie_"
                        r"funkcji_do_klasy_lub_instancji/export_static.csv", ["Brand", "Model", "IsOnSale"],
                        [car_01.brand, car_01.model, car_01.IsOnSale])
print(dir(Car))

print("Class------" * 5)
Car.ExportToFile_Class = types.MethodType(exportToFile_Class, Car)
Car.ExportToFile_Class(path=r"/media/sf_phyton_nauka/kurs udemy/srednio_zaawansowany/cwicze5_9_dynamiczne_dolaczanie_funkcji_do_klasy_lub_instancji/export_Class.csv")
print(dir(Car))

print("Class------" * 5)
Car.ExportToFile_Instance = types.MethodType(exportToFile_Instance, car_01)
Car.ExportToFile_Instance(path=r"/media/sf_phyton_nauka/kurs udemy/srednio_zaawansowany/cwicze5_9_dynamiczne_dolaczanie_funkcji_do_klasy_lub_instancji/export_Instance.csv")
print(dir(car_01))

print("-----" * 10)
if hasattr(car_01, "ExportToFile_Static") and callable(car_01.ExportToFile_Static):
    print("The object has method ExportofFile_Static")
if hasattr(car_01, "ExportToFile_Class") and callable(car_01.ExportToFile_Class):
    print("The object has method ExportofFile_Class")
if hasattr(car_01, "ExportToFile_Instance") and callable(car_01.ExportToFile_Instance):
    print("The object has method ExportofFile_Instance")
if hasattr(car_01, "IsOnSale") and callable(car_01.IsOnSale):
    print("The object has method ExportofFile_Instance")
else:
    print("No such method")"""


import csv
import types


def exportToFile_Static(path, header, data):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
    print("Information was exported to file - static method")


def exportToFile_Class(cls, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["brand", "model", "IsOnSale"])
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])
    print("Information was exported to file - class method")


def exportToFile_Instance(self, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["brand", "model", "IsOnSale"])
        writer.writerow([self.brand, self.model, self.IsOnSale])
    print("Information was exported to file - instance method")


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

print("Static -----" * 5)
Car.ExportToFile_Static = exportToFile_Static
## exportToFile_Static(r"/media/sf_phyton_nauka/kurs udemy/srednio_zaawansowany/cwicze5_9_dynamiczne_dolaczanie_funkcji_do_klasy_lub_instancji/export_static.csv", ["Brand", "Model", "IsOnSale"], [car_01.brand, car_01.model, car_01.IsOnSale])
Car.ExportToFile_Static(r"/media/sf_phyton_nauka/kurs udemy/srednio_zaawansowany/cwicze5_9_dynamiczne_dolaczanie_funkcji_do_klasy_lub_instancji/export_static.csv", ["Brand", "Model", "IsOnSale"], [car_01.brand, car_01.model, car_01.IsOnSale])
print(dir(Car))

print("Class------" * 5)
## Car.ExportToFile_Class = exportToFile_Class
Car.ExportToFile_Class = types.MethodType(exportToFile_Class, Car)
Car.ExportToFile_Class(path=r"/media/sf_phyton_nauka/kurs udemy/srednio_zaawansowany/cwicze5_9_dynamiczne_dolaczanie_funkcji_do_klasy_lub_instancji/export_Class.csv")
print(dir(Car))

print("Class------" * 5)
## Car.ExportToFile_Instance = exportToFile_Instance
Car.ExportToFile_Instance = types.MethodType(exportToFile_Instance, car_01)
Car.ExportToFile_Instance(path=r"/media/sf_phyton_nauka/kurs udemy/srednio_zaawansowany/cwicze5_9_dynamiczne_dolaczanie_funkcji_do_klasy_lub_instancji/export_Instance.csv")
print(dir(car_01))

print("-----" * 10)
if hasattr(car_01, "ExportToFile_Static") and callable(car_01.ExportToFile_Static):
    print("The object has method ExportofFile_Static")
if hasattr(car_01, "ExportToFile_Class") and callable(car_01.ExportToFile_Class):
    print("The object has method ExportofFile_Class")
if hasattr(car_01, "ExportToFile_Instance") and callable(car_01.ExportToFile_Instance):
    print("The object has method ExportofFile_Instance")
if hasattr(car_01, "IsOnSale") and callable(car_01.IsOnSale):
    print("The object has method ExportofFile_Instance")
else:
    print("No such method")