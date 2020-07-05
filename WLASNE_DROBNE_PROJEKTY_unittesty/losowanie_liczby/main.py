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

# modernizacja
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