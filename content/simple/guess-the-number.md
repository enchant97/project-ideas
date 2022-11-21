---
title: "Guess the Number"
description: "A programming project about building a Guess the Number app"
draft: true
author: JamesClarke7283
---

## Intro

This program is an implementation of the classic guess The number game.

Where a player has 5 tries to guess a number between 1 and 20.

## Requirements

- Generate a random number in a range of x to y.

- Get user input of guess.

- compare and return if correct or not

- if not correct, tell user if too high or too low. and decrement number of lives.

- if correct, congratulate the user and, exit program.

- if number of lives is below 1, tell the user and exit.

## Guide

create a procedure whereby if the guess is greater than answer, it will return "too high". and if guess is less than answer it will return "too low".



1. import a 'random', library you will need that later when you define a random number to guess.

2.  Define constants for 'RANGE_START' and 'RANGE_END' which is the  start and end range for the answer number to be generated.

3. Define a lives variable set it to 5, or whatever you want the starting lives to be.

4. define a number variable, generate a random int which is between RANGE_START and RANGE_END, then set the number variable to it.

5. Create an infinate while loop (While True may surffice)

6. Create a guess input variable and set it to the output of the input prompt function (stdin).

7. ***[EXTRA]*** Try and catch ValueErrors and if one occors put in, 'Incorrect type, must be a whole number between [RANGE_START_HERE] and [RANGE_END_HERE]'

8. check if lives less than one, if it is, print 'Ran out of lives, you lost', then break out of the loop.

9. Write an if which checks if guess is greater than RANGE_END or is less than RANGE_START. if so, print error 'OutOfRange: Type a number between [RANGE_START] and [RANGE_END]' then write a continue so it brings you back to the top of the loop.

10. check if guess is equel to number, if so, print a congratulations message like '[guess] was correct!! you won with [lives] lives remaining' then break out of the loop. else print a failure message and decrement the number of lives.



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

#### Erronious interaction: Out of Range

```
Guess The Number [5 lives]:	50
ERROR:	OutOfRange: Type a number between 1 and 20
Guess The Number [5 lives]:	
```

#### Erronious interaction: ValueError

```
Guess The Number [5 lives]:	test
Incorrect type, must be a whole number between 1 and 20
Guess The Number [5 lives]:	
```

## Extra

- Make user pick starting number of lives/difficulty level. At start of game.

- Pick START/END range of game with environment variables.

- Save High Score/Streak to a file.
