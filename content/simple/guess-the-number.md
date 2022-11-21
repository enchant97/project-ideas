---
title: "Guess the Number"
description: "A programming project about building a guess the number app"
author: JamesClarke7283
---
## Intro
This project will be the classic "guess the number" game. This is where a player has a set number of tries to guess a number between a given range.


## Requirements
- Generate a random number in a set range (should be known to user)
- Get user input of guess
- Compare and output if correct or not
- If not correct, tell user if too high or too low and decrement number of lives.
- If correct, congratulate the user and exit
- If number of lives is below 1, tell the user and exit
- *Extra*: handle possible errors


## Guide
1.  Define two variables; these will contain the start and end range
    - Choose a int type if your language is statically typed
    - Define as a constant if possible in your language
    - Suggested names: `RANGE_START`, `RANGE_END`
    - Example value: `RANGE_START=1`, `RANGE_END=20`
2. Define a variable to store the remaining lives (default value will be starting lives).
   - Choose a int type if your language is statically typed
   - Suggested name: `lives`
   - Example value: `5`
3. Define a variable which will store the number to guess
    - Choose a int type if your language is statically typed
    - Suggested name: `number`
4. Set `number` to a random number in the range `RANGE_START` to `RANGE_END`
5. Create a infinite while loop
    1. Define a variable to store the guess
        - Suggested name: `guess_input`
        - Choose a string type if your language is statically typed
    2. Output message prompting user to guess number e.g. "Guess the number: "
    3. Get input from user and store in `guess_input`
    4. Define a variable to store the guess as a number
        - Choose a int type if your language is statically typed
        - Suggested name: `guess`
    5. Convert `guess_input` to int and store in `guess`
        - *Extra*: handle possible errors for user input
            - Output error to user
            - Restart to start of loop if error occurred
    6. Check if number is equal to `number`
        1. Output message saying it was correct
        2. *Extra*: Output lives remaining
        3. Break out of loop
    7. Check if number is greater than `number`
        1. Output that guess was too high
        2. Subtract 1 from `lives`
    8. Check if number is less than `number`
        1. Output that guess was too low
        2. Subtract 1 from `lives`
    9. Check if lives is less than 1
        1. Output that the user has no lives left
        2. Output the actual number
        3. Break out of loop
    10. Loop!
6. Program finished


## Running
{{< project/run-intro >}}

### Example Interactions
#### Losing Interaction
```
Guess The Number [5 lives]:	10
Incorrect, 10 was too low, Try again
Guess The Number [4 lives]:	20
Incorrect, 20 was too high, Try again
Guess The Number [3 lives]:	17
Incorrect, 17 was too high, Try again
Guess The Number [2 lives]:	16
Incorrect, 16 was too high, Try again
Guess The Number [1 lives]:	15
Incorrect, 15 was too high, Try again
Guess The Number [0 lives]:	17
Ran out of lives, you lost
```

#### Winning Interaction
```
Guess The Number [5 lives]:	10
Incorrect, 10 was too high, Try again
Guess The Number [4 lives]:	5
Incorrect, 5 was too low, Try again
Guess The Number [3 lives]:	6
Incorrect, 6 was too low, Try again
Guess The Number [2 lives]:	7
Incorrect, 7 was too low, Try again
Guess The Number [1 lives]:	8
8 was correct!! you won with 1 lives remaining
```

#### Erroneous Interaction: Out of Range
```
Guess The Number [5 lives]:	50
ERROR:	OutOfRange: Type a number between 1 and 20
Guess The Number [5 lives]:
```

#### Erroneous Interaction: Value Error
```
Guess The Number [5 lives]:	test
Incorrect type, must be a whole number between 1 and 20
Guess The Number [5 lives]:
```


## Extra
- Implement the steps indicated with "*Extra*"
- Make user pick starting number of lives/difficulty level. At start of game.
- Save High Score/Streak to a file.
- Take a look at the example solutions, *you could learn how to write it in a different language*
