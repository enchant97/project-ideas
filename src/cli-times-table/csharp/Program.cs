//
// CLI Times Table C# Solution
// Made On: net6.0
//

// Output & collect user input, store in times_table_input variable
Console.Write("Enter times table: ");
string times_table_input = Console.ReadLine();
// Convert times_table_input string into a int
uint times_table = uint.Parse(times_table_input);

// Output & collect user input, store in table_range variable
Console.Write("Enter range (e.g. 1-12): ");
string table_range = Console.ReadLine();

// Split the table_range string into a list, using "-" as the separator
string[] table_range_split = table_range.Split("-"); // e.g. ["1", "12"]

// Access the values from the list by their index's and convert to ints
uint start = uint.Parse(table_range_split[0]);
uint end = uint.Parse(table_range_split[1]);

// Add one as start users start from 1 not 0
end += 1; // Shorter than: 'end = end + 1'

// Output using string interpolation
Console.WriteLine($"Times Table For {times_table}, {table_range}:");

// For loop x will increment from "start" to "end"
for (uint x = start; x < end; x++)
{
    // Multiply times_table with x and store in result
    uint result = times_table * x;
    // Output using string interpolation
    Console.WriteLine($"  {x} x {times_table} = {result}");
}
