# praca z funkcjami jak ze zmiennymi
def BuyMe(what):
    print("Give me ", what)


BuyMe("a nwe car")

StealForMe = BuyMe      # podstawienie zmiennej jako funkcji
print(type(StealForMe))
StealForMe("a new car")     #urucheminie przypisanej zmiennej przypisanej do funkcji

# przyklad automatycznej restauracji
def GoLeft(*args):
    print("PLACEHOLDER - turning left with", *args)

def GoRight(*args):
    print("PLACEHOLDER - turning right with", *args)

def GoFoward(*args):
    print("PLACEHOLDER - going foward with", *args)

def GoBack(*args):
    print("PLACEHOLDER - going back with", *args)

def Start(*args):
    print("PLACEHOLDER - starting with", *args)

def Stop(*args):
    print("PLACEHOLDER - stopping with", *args)
# placeholder czyli miejsce ktore trzeba uzupelnic
# kazda z powyzszych funkcji moze byc kilkakrtonie wywolywana albo wcale

# lista instrukcji dla kazdego "robota
instructions = [Start, GoFoward, GoFoward, GoLeft, GoFoward,GoRight, Stop]

dish = "pizza"      #zmienna wskazujaca na danie
for instr in instructions:          # dla kazdej instrukcji w liscie instrukcje nalezy wykonac dana instrukcje i
    # wywolac odpowiednia instrukcje przekazujac do niej parametr dish
    instr(dish)