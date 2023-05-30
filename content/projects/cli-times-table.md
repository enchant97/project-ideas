---
title: "CLI Times Table"
description: "A programming project about building a cli times table app"
tags: ["simple"]
---
## Intro
This project will be a cli app to calculate the times table with a given range.


## Requirements
- Ask times table number from user e.g. "1"
- Ask for a range e.g. "1-12" to calculate
  - *Extra*: if no range is given default to "1-12"
- Output times table in a easily readable format e.g. "1 x 1 = 1"
  - *Extra*: make output look like a table
- *Extra*: handle input errors


## Guide
1. Create variable to store times table number
    -  Choose a int type if your language is statically typed
    -  Name it `times_table`
2. Output "`Enter times table: `" to the console
3. Accept input from console, converting to a int and storing into `times_table`
4. Create a variable to store the range input
    - Choose a string type if your language is statically typed
    - Name it `table_range`
5. Output "`Enter range (e.g. 1-12): `" to the console
6. Accept input from console storing into `table_range`
7. Create a variable
    - Choose an string array/list type, if a length is needed use 2
    - Name it `table_range_split`
8. Split the `table_range`, using "`-`" as the separator, store result in `table_range_split`
9. Create two variables
   - Choose a int type if your language is statically typed
   - Name them `start` and `end`
10. Convert index 0 of `table_range_split` into a int and store in `start`
11. Convert index 1 of `table_range_split` into a int and store in `end`
12. Output message saying what the selected times table is, including the selected range
13. Create a for loop; this should use a range from the `start` `stop` variables
    1.  Create variable
        - Choose a int type if your language is statically typed
        - Name it `result`
    2. Multiply `times_table` with `i` and store in `result`
    3. Output times table result
14. Program finished


## Running
{{< project/run-intro >}}

### Example Interactions
```
Enter table number: 2
Enter range (e.g. 1-12): 1-5
Times Table For 2, 1-6:
  1 x 2 = 2
  2 x 2 = 4
  3 x 2 = 6
  4 x 2 = 8
  5 x 2 = 10
```


## Extra
- Implement the steps indicated with "*Extra*"
- Take a look at the example solutions, *you could learn how to write it in a different language*
