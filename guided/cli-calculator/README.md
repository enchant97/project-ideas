# CLI Calculator
This will be a calculator that can take in two numbers from the user and calculate an answer with a given operation (add or subtract).

## Requirements
- Get two numbers from the user as separate variables
- *Extra*: Validate user input
- Convert numbers input into a float
- Get operator from user, for example: add or subtract
- Do “math” with selected operator
- Store result in a variable
- Output the result


## Guide
1. Create two variables that will be used to store the input numbers
   - Choose a float type if your language is statically typed
   - These two variables could be called "num_a" and "num_b"
2. Output "Enter Number A: " to console
3. Accept input from console, converting to a float and storing in the "num_a" variable
   1. *Extra*: check if input entered is a valid float, if not exit with a error message
4. Repeat 2 & 3, but store in "num_b"
5. Create a variable called "operator", this will be a string type
6. Output "Do you want to (add) or (subtract)? " to console
7. Accept input from console and store into "operator" variable
8. Create a variable called "result" that will be a float type
9.  Create a if statement that checks for the "operator" variable equalling "add"
   1.  Add variable "num_a" and "num_b" together (num_a + num_b)
   2.  Store the result in "result" variable
   3.  Output "result" variable to console
10. Create a elif/else if statement that checks for the "operator" variable equalling "subtract"
    1.  Subtract variable "num_b" from "num_a" (num_a - num_b)
    2.  Store the result in "result" variable
    3.  Output "result" variable to console
11. Create an else statement
    1.  Output "Invalid operator given"
12. Program finished


## Run It
Once completed test your code with some data, if it does not work try having a look at a working example solution and compare your code.

Please be aware example solutions may not look the same as your code, don't panic if your code works but does not look the same. There are many different ways of implementing the solution(s).

### Example Interactions
Here is what a finished solution should look like to a user

#### Add

```
Enter Number A: 1
Enter Number b: 2
Do you want to (add) or (subtract)? add
3
```

#### Invalid

```
Enter Number A: 1
Enter Number b: 2
Do you want to (add) or (subtract)? hello
Invalid operator given!
```


## Finished?
- Implement the steps indicated with "*Extra*"
- Add multiplying and dividing
- Accept more than two numbers
- Handle invalid inputs better, *add a loop and keep asking until user enters correct value*
- Make the result output more user friendly, e.g "Result num_a + num_b = result"
- Take a look at the example solutions, *you could learn how to write it in a different language*
