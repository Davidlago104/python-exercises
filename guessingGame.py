# Guessing game where the user has to guess a number between 1 and 100.
# The program gives feedback on whether the guess is too low, too high, or correct.
# The game continues until the user guesses the correct number.
import random

number_to_guess = random.randint(1, 100)

while True:
    user_guess = int(input("Guess a number between 1 and 100: "))
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the correct number!")
        break