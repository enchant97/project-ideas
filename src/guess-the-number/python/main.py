#
# CLI Guess The Number Game
# Made On: Python 3.10
# Author: JamesClarke7283
# SPDX-License-Identifier: MIT
#
import random


def high_or_low_guess(guess, answer):
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
    guess_input = input(f"Guess The Number [{lives} lives]: ")
    try:
        # Casts guess to an int & stores it in 'guess'
        guess = int(guess_input)

        if guess > RANGE_END or guess < RANGE_START:
            # Checks to see if user has gone out of number range,
            # if so it prints an error and continues to top of loop
            print(f"ERROR:\tOutOfRange: Type a number between {RANGE_START} and {RANGE_END}")
            continue
        if guess == number:
            # Checks to see if the guess was correct,
            # if so prints a congratulations message and exits
            print(f"{guess} was correct!! you won with {lives} lives remaining")
            break
        else:
            # Guess does not match
            # Get either 'too high' or 'too low' output
            high_or_low = high_or_low_guess(guess, number)
            print(f"Incorrect, {guess} was {high_or_low}, Try again")
            # subtract 1 from lives
            lives -= 1

        # Checks to see if lives is less than 1,
        # if so it prints a fail message & breaks out the loop
        if lives < 1:
            print(f"Ran out of lives, you lost. The number was: {number}")
            break

    except ValueError:
        # handle error when that may happen
        # when converting an invalid number from user
        print(f"Incorrect type, must be a whole number between {RANGE_START} and {RANGE_END}")
