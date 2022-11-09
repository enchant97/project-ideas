#!/usr/bin/env perl
#
# CLI Times Table Perl Solution
# Made On: Perl 5.36
#
print "Enter table number: ";
$times_table = <>;
chomp($times_table);

print "Enter range (e.g. 1-12): ";
$table_range = <>;
chomp($table_range);

@table_range_split = split("-", $table_range, 2);

$start = @table_range_split[0];
$end = @table_range_split[1] + 1;

print "Times Table For ${times_table}, ${table_range}:\n";

for ($x = $start; $x < $end; $x ++)
{
    $result = $times_table * $x;
    print "  ${x} x ${times_table} = ${result}\n";
}
