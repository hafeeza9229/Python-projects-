"""
take inputs of lower and higher bound of range.
compiler generates a number.
user guesses the number.
if number is same loop will end otherwise user will be given 7 attempts

"""

import random

print("Welcome to the Number Guessing Game \nYou got 7 chances to guess the number.\nLet's start the game ")

lower_bound = input("Enter lower bound:")
upper_bound = input("Enter upper bound:")

number_to_guess = random.randrange(int(lower_bound), int(upper_bound))
print(number_to_guess)

counter = 7
end_counter = 0
while True:
    if counter >= end_counter:
        user_guess = int(input("Please enter your guess:"))
        if user_guess == number_to_guess:
            print(f"The number to guess is {number_to_guess}.Congratulations! You found it right.")
            break
        elif user_guess > number_to_guess:
            print("Try again! You guessed too high.")
        elif user_guess < number_to_guess:
            print("Try again! You guessed too low.")
        counter -= 1
    else:
        print(f"Oops! Better luck next time. The number to guess is {number_to_guess}")
        break
