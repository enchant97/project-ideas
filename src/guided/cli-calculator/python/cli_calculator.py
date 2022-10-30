#
# CLI Calculator Python Solution
# Made On: Python 3.10
#

# Output & collect user input, store in temp_a variable
temp_a = input("Enter Number A: ")
# Convert the inputed data into a float, store in num_a variable
num_a = float(temp_a)

# Output & collect user input, store in temp_b variable
temp_b = input("Enter Number B: ")
# Convert the inputed data into a float, store in num_b variable
num_b = float(temp_b)

# Output & collect user input, store in operator variable
operator = input("Do you want to (add) or (subtract)? ")

# Check if operator is equal to "add"
if operator == "add":
    # add num_a and num_b together, store in result variable
    result = num_a + num_b
    # output the result variable data to console
    print(result)
# Above statement(s) did not match so check if operator is equal to "subtract"
elif operator == "subtract":
    # subtract num_b from num_a, store in result variable
    result = num_a - num_b
    # output the result variable data to console
    print(result)
# Operator does not match any of above statements
else:
    # output the error message
    print("Invalid operator given!")
