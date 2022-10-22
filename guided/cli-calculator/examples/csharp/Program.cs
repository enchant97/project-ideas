//
// CLI Calculator C# Solution
// Made On: net6.0
//

Console.Write("Enter Number A: ");
var temp_a = Console.ReadLine();
var num_a = float.Parse(temp_a);

Console.Write("Enter Number B: ");
var temp_b = Console.ReadLine();
var num_b = float.Parse(temp_b);

Console.Write("Do you want to (add) or (subtract)? ");
var operator_ = Console.ReadLine();

if (operator_ == "add")
{
    var result = num_a + num_b;
    Console.WriteLine(result);
}
else if (operator_ == "subtract")
{
    var result = num_a - num_b;
    Console.WriteLine(result);
}
else
{
    Console.WriteLine("Invalid operator given!");
}
