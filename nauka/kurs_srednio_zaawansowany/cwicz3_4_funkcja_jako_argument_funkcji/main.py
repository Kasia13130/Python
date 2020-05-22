
def Bake(what):
    print("Baking {}".format(what))

def Add(what):
    print("Adding {}".format(what))

def Mix(what):
    print("Mixing {}".format(what))


cookbook = [(Add, "milk"), (Add, "eggs"), (Add, "flour"), (Add, "sugar"), (Mix, "ingredients"), (Bake, "cookies")]


for activity, obj in cookbook:
    activity(obj)

print("@" * 30)


def Cook(activity, obj):
    activity(obj)

Cook(Bake, "brownies")


for activity, obj in cookbook:
    Cook(activity, obj)

