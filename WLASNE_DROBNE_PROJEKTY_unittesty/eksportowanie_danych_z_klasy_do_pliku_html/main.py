import types


def export_1_cake_to_html(obj, path):
    template = """
<table border=1>        
     <tr>                      
       <th colspan=2>{}</th>       
     </tr>
       <tr>
         <td>Kind</td>              
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Weight [kg]</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Price[zl]</td>
         <td>{}</td>
       </tr>
</table>"""                     

    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additions, obj.filling, obj.weight, obj.price)
        f.write(content)


def export_all_cake_to_html(cls, path):
    template_header = """       
<table border=1>"""
    template_data = """         
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Weight [kg]</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Price [zl]</td>
         <td>{}</td>
       </tr>"""
    template_footer = """           
</table>"""

    with open(path, "w") as f:
        f.write(template_header)
        for b in cls.bakery_offer:
            content = template_data.format(b.name, b.kind, b.taste, b.additions, b.filling, b.weight, b.price)
            f.write(content)

        f.write(template_footer)


def export_this_cake_to_html(self, path):
    template = """
<table border=1>
         <tr>
           <th colspan=2>{}</th>
         </tr>
           <tr>
             <td>Kind</td>
             <td>{}</td>
           </tr>
           <tr>
             <td>Taste</td>
             <td>{}</td>
           </tr>
           <tr>
             <td>Additives</td>
             <td>{}</td>
           </tr>
           <tr>
             <td>Filling</td>
             <td>{}</td>
           </tr>
           <tr>
             <td>Weight [kg]</td>
             <td>{}</td>
           </tr>
           <tr>
             <td>Price [zl]</td>
             <td>{}</td>
           </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.additions, self.filling, self.weight,
                                  self.price)
        f.write(content)


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
        self.additions = additions.copy()
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
            for a in self.additions:
                print("Additives:\t{}".format(a.split(",")))

        if self.filling != " ":
            print("Filling: {}".format(self.filling))

        if self.__gluten_free:
            print("Gluten free: {}".format("Yes"))
        else:
            print("Gluten free: {}".format("No"))

        if self.kind == "cake" and self.__text != "":
            print("Text on baking: {}".format(self.__text))
        elif self.kind == "cake" and self.__text == "":
            print("".format(self.Text))

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additions):
        self.additions.append(additions)

    def __get_text(self):
        print("Text on baking: {}".format("Happy Birthday:)"))
        return self.__text

    def __set_text(self, new_text):
        if self.__text == "cake" in self.kind:
            print("Status {} to {}".format(new_text, self.kind))

    Text = property(__get_text, __set_text, None, "Baking text")


cake_01 = Cake("Chocolate Cherry", "cake", "chocolate", ["sponge cake", "cherries", "icing"], "chocolate", 0.2, 9,
               False, "Happy birthday!!")
cake_02 = Cake("Coconut", "cookies", "sweet", ["coconut", "cocoa topping"], " ", 0.05, 6.50, True, "")
cake_03 = Cake("Oranges", "cake", "sweet-sour", ["pieces of orange"], "orange mus, cream filling", 0.3, 4, False,
               "Happy birthday :)")
cake_04 = Cake("Cocoa waffle", "waffle", "cocoa", [], "cocoa", 0.8, 4, False, "")


Cake.export_1_cake_to_html = export_1_cake_to_html
Cake.export_1_cake_to_html(cake_01, r"/media/sf_phyton_nauka/kurs udemy/srednio_zaawansowany/cwicze5_9_dynamiczne_"
                                    r"dolaczanie_funkcji_do_klasy_lub_instancji/cwiczenie/cake_01.html")

Cake.export_all_cake_to_html = types.MethodType(export_all_cake_to_html, Cake)
Cake.export_all_cake_to_html(r"/media/sf_phyton_nauka/kurs udemy/srednio_zaawansowany/cwicze5_9_dynamiczne_"
                             r"dolaczanie_funkcji_do_klasy_lub_instancji/cwiczenie/class_cake.html")

for x in Cake.bakery_offer:
    Cake.export_this_cake_to_html = types.MethodType(export_this_cake_to_html, x)

for x in Cake.bakery_offer:
    Cake.export_this_cake_to_html(r"/media/sf_phyton_nauka/kurs udemy/srednio_zaawansowany/cwicze5_9_dynamiczne_"
                                  r"dolaczanie_funkcji_do_klasy_lub_instancji/cwiczenie/{}.html"
                                  .format(x.name.replace(" ", "_")))



