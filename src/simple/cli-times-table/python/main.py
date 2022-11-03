#
# CLI Times Table Python Solution
# Made On: Python 3.10
#

# Output & collect user input, store in times_table variable
times_table = input("Enter table number: ")
# Convert times_table string into a int
times_table = int(times_table)

# Output & collect user input, store in table_range variable
table_range = input("Enter range (e.g. 1-12): ")

# split the table_range string into a list, using "-" as the separator
table_range_split = table_range.split("-")  # e.g. ["1", "12"]

# Access the values from the list by their index's and convert to ints
start = int(table_range_split[0])
end = int(table_range_split[1])

# add 1 to "end" so python's range will end at the correct number
end += 1  # shorter than: 'end = end + 1'

# Output f-string
print(f"Times Table For {times_table}, {table_range}:")

# For loop x will increment from "start" to "end"
for x in range(start, end):
    # multiply times_table with x and store in result
    result = times_table * x
    # Output f-string
    print(f"  {x} x {times_table} = {result}")
