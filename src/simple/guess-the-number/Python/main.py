#
# CLI Guess The Number Game
# Made On: Python 3.10
# Author: Copyright (C) James Clarke <james@james-clarke.ynh.fr>
import random


def comp_incorrect(guess, answer):
    if guess > answer:
        return "too high"
    elif guess < answer:
        return "too low"


# Constants Section, defines start and end
RANGE_START = 1
RANGE_END = 20

lives = 5

number = random.randint(RANGE_START, RANGE_END)
while True:
    # Receives input from the user as a string
    guess_inp = input(f"Guess The Number [{lives} lives]:\t")
    try:
        # Casts guess to an int & stores it in guess
        guess = int(guess_inp)
        # Checks to see if lives is less than 1, if so it prints a fail message & breaks out the loop
        if lives < 1:
            print("Ran out of lives, you lost")
            break
        # Checks to see if user has gone out of number range, if so, it prints an error and continues to top of loop
        if guess > RANGE_END or guess < RANGE_START:
            print(f"ERROR:\tOutOfRange: Type a number between {RANGE_START} and {RANGE_END}")
            continue
            # Checks to see if the guess was correct, if so, prints a congratulations message and exits
        elif guess == number:
            print(f"{guess} was correct!! you won with {lives} lives remaining")
            break
        else:
            print(f"Incorrect, {guess} was {comp_incorrect(guess, number)}, Try again")
        lives -= 1
    except ValueError:
        print(f"Incorrect type, must be a whole number between {RANGE_START} and {RANGE_END}")
