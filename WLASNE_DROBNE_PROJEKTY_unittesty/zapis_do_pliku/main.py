import pickle
import glob


class Cake:

    known_types = ["cake", "cookies", "muffins", "other"]
    bakery_offer = []

    def __init__(self, name, kind, taste, additions, filling, weight, price, gluten_free, text):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = "other"
        self.taste = taste
        self.additions = additions
        self.filling = filling
        self.weight = weight
        self.price = price
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        self.__text = text
        if self.kind == "cake" or text == "":
            self.__text = text
        else:
            print("Error in: {}".format(name))

    def show_info(self):
        print("\n{}".format(self.name).upper())
        print("Kind: {}".format(self.kind))
        print("Taste: {}".format(self.taste))

        if self.additions != " ":
            print("Additives: ")
            for a in self.additions:
                print("\t{}".format(a))

        if self.filling != " ":
            print("Filling: {}".format(self.filling))

        if self.__gluten_free:
            print("Gluten free: {}".format("Yes"))
        else:
            print("Gluten free: {}".format("No"))

        if self.kind == "cake" and self.__text != "":
            print("Text on baking: {}".format(self.__text))
        elif self.kind == "cake" and self.__text == "":     # wyswietlenie tylko tekstu z wlasciwosci Text
            print("".format(self.Text))

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additions.append(additives)

    def __get_text(self):
        print("Text on baking: {}".format("Happy Birthday:)"))
        return self.__text

    def __set_text(self, new_text):
        if self.__text == "cake" in self.kind:
            print("Status {} to {}".format(new_text, self.kind))

    Text = property(__get_text, __set_text, None, "Baking text")

    def save_to_file(self, path):
        with open(path, "wb") as f:
            pickle.dump(self, f)        # jesli zapisujemy jakis obiekt do pliku to trzeba pamietac ze pracujemy na instancji wiec trzeba dopisac self

    @classmethod
    def read_from_file(cls, path):
        with open(path, "rb") as f:
            new_obj = pickle.load(f)
            cls.bakery_offer.append(new_obj)
            return new_obj

    @staticmethod
    def get_bakery_files(catalog):
        return glob.glob(catalog + "/*.bakery")


cake_01 = Cake("Chocolate Cherry", "cake", "chocolate", ["sponge cake", "cherries", "icing"], "chocolate", 0.2, 9, False, "Happy birthday!!")
cake_02 = Cake("Coconut", "cookies", "sweet", ["coconut", "cocoa topping"], " ", 0.05, 6.50, True, "")
cake_03 = Cake("Oranges", "cake", "sweet-sour", ["pieces of orange"], "orange mus, cream filling", 0.3, 4, False, "Happy birthday :)")
cake_04 = Cake("Cocoa waffle", "waffle", "cocoa", [], "cocoa", 0.8, 4, False, "")

cake_01.save_to_file("/media/sf_phyton_nauka/kurs udemy/srednio_zaawansowany/cwicz5_7_metody_instancji_klasy_i_"
                     "statyczne/cwiczenie/cake_01.bakery")
cake_02.save_to_file("/media/sf_phyton_nauka/kurs udemy/srednio_zaawansowany/cwicz5_7_metody_instancji_klasy_i_"
                     "statyczne/cwiczenie/cake_02.bakery")
cake_05 = cake_01.read_from_file("/media/sf_phyton_nauka/kurs udemy/srednio_zaawansowany/cwicz5_7_metody_instancji_"
                                 "klasy_i_statyczne/cwiczenie/cake_01.bakery")


print("Today in our offer:")
for x in Cake.bakery_offer:
    x.show_info()

print(Cake.get_bakery_files("/media/sf_phyton_nauka/kurs udemy/srednio_zaawansowany/cwicz5_7_metody_instancji_"
                                 "klasy_i_statyczne/cwiczenie"))
print(Cake.get_bakery_files("/media/sf_phyton_nauka/kurs udemy/srednio_zaawansowany/cwicz5_7_metody_instancji_"
                                 "klasy_i_statyczne/cwiczenie"))
