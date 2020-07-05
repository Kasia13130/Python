
def calculate_paint(efficency_ltr_per_m2, *surface):

    allSurface = 0

    for s in surface:

        amount = efficency_ltr_per_m2 * s
        allSurface += amount
        return allSurface


print(calculate_paint(1.5, 6, 12, 8))


surface = [5, 8, 10]
print(calculate_paint(1.5, *surface))


# ----------
file = r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz3_2_argumenty_specjalne_args_kwards\cwiczenie\text.txt"


def log_it(*args):
    with open("text.txt", "a") as t:
        for a in args:
            t.write(a)
            t.write(" ")
        t.write("\n")


log_it("Starting processing forecasting")
log_it("ERROR", "Not enough data", "invoices", "2020")

