cargo = [40, 20, 4, 5, 30, 8, 2, 7, 3, 19, 32, 40, 20, 35, 15, 32, 9]
cargo.sort()
cargo.reverse()

print("The cargo list is :", cargo)

boxCapacity = 90
box = []
i = 0

while i < len(cargo) and (boxCapacity - sum(box)) >= min(cargo):
    if (boxCapacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i += 1

print("The collected items sum is:", sum(box))
print("The elements are:", box)

print("\n")

# cwiczenie
number = 1
previous_number = 0

while number <= 50:
    print(number + previous_number)
    previous_number = number
    number += 1

print("\n")

# cwiczenie 2 i 3

import random
my_number = random.randint(0, 20)
guess = -1

print("Guess my number")

while guess != my_number:

    guess = int(input())

    if guess == my_number:
        print("Gratulations! It was:", my_number, )
    elif guess >= my_number:
        print("Sorry - my number is smaller than", guess, "Try again!")
    else:
        print("Sorry- my number is greater than", guess, "Try again!")

# cwiczenie 3
import random
my_number = random.randint(0, 20)
guess = -1
trials = 0
print("Guess my number")

while guess != my_number:

    guess = int(input())

    if guess == my_number:
        print("Gratulations! It was:", my_number, trials)
    elif guess >= my_number:
        print("Sorry - my number is smaller than", guess, "Try again!")
    else:
        print("Sorry- my number is greater than", guess, "Try again!")

    trials += 1