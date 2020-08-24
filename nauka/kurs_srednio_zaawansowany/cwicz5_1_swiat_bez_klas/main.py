carBrand = "Seat"
carModel = "Ibiza"
carIsAirBagOk = True
carIsPaintingOk = True
carIsMechanicOk = True


def IsCarDamage(carIsAirBagOk, carIsPaintingOk, carIsMechanicOk):
    return not (carIsAirBagOk and carIsPaintingOk and carIsMechanicOk)


print(IsCarDamage(carIsAirBagOk, carIsPaintingOk, carIsMechanicOk))
print("\n")


# ------

car_01 = {
    "carBrand": "Seat",
    "carModel": "Ibiza",
    "carIsAirBagOk": True,
    "carIsPaintingOk": True,
    "carIsMechanicOk": True
}


def IsCarDamage(carIsAirBagOk, carIsPaintingOk, carIsMechanicOk):
    return not (carIsAirBagOk and carIsPaintingOk and carIsMechanicOk)


print(IsCarDamage(car_01["carIsAirBagOk"], car_01["carIsPaintingOk"], car_01["carIsMechanicOk"]))
print("\n")

# --------

car_01 = {
    "carBrand": "Seat",
    "carModel": "Ibiza",
    "carIsAirBagOk": True,
    "carIsPaintingOk": True,
    "carIsMechanicOk": True
}


def IsCarDamage(aCar):
    return not (aCar["carIsAirBagOk"] and aCar["carIsPaintingOk"] and aCar["carIsMechanicOk"])


print(IsCarDamage(car_01))
print("\n")

# ---------

car_01 = {
    "carBrand": "Seat",
    "carModel": "Ibiza",
    "carIsAirBagOk": True,
    "carIsPaintingOk": True,
    "carIsMechanicOk": True
}

car_02 = {
    "carBrand": "Opel",
    "carModel": "Corsa",
    "carIsAirBagOk": True,
    "carIsPaintingOk": False,
    "carIsMechanicOk": True
}


def IsCarDamage(aCar):
    return not (aCar["carIsAirBagOk"] and aCar["carIsPaintingOk"] and aCar["carIsMechanicOk"])


print(IsCarDamage(car_01))
print(IsCarDamage(car_02))

cars = [car_01, car_02]
for c in cars:
    print("{} {} damage = {}".format(c["carBrand"], c["carModel"], IsCarDamage(c)))
