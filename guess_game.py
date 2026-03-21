import random

number = random.randint(1, 100)
guess = None

print("Welcome to the Number Guessing Game!")

while guess != number:
    guess = int(input("Enter a number between 1 and 100: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number!")