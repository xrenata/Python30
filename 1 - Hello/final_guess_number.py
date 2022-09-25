import random

num = random.randint(1, 20)
guess = None

while guess != num:
    guess = input("Guess a number between 1 and 20: ")
    guess = int(guess)

    if guess == num:
        print("Congratulations!")
        break
    else:
        print("Try again!")
