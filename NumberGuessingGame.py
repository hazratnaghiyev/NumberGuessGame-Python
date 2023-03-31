import random

number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 10: "))

while guess != number:
    if guess < number:
        print("Try again, entered number is too low!")
    else:
        print("Try again, entered number is too high!")

    guess = int(input("Try again: "))

    print("Congratulation! You guessed the number!")
    break