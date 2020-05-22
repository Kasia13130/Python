import random

min = 1
max = 6
dice = random.choice(range(min, max))

if dice == 1:
    print("%3s" % ("o"))
elif dice == 2:
    print("%3s \n \n%s" % ("o", "o"))
elif dice == 3:
    print("%3s \n%2s \no" % ("o", "o"))
elif dice == 4:
    print("o %3s \n \no %3s" % ("o", "o"))
elif dice == 5:
    print("o %3s \n%3s \no %3s" % ("o", "o", "o"))
else:
    print("o %3s \no %3s \no %3s" % ("o", "o", "o"))