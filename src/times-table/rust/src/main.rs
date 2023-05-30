//
// CLI Times Table Rust Solution
// Made On: Rust 2021
//

use std::io;

fn main() {
    println!("Enter times table number:");
    let mut times_table_input = String::new();
    io::stdin().read_line(&mut times_table_input).unwrap();
    times_table_input = times_table_input.strip_suffix("\n").unwrap().to_string();
    let times_table = times_table_input.parse::<usize>().unwrap();

    println!("Enter range (e.g. 1-12):");
    let mut table_range_input = String::new();
    io::stdin().read_line(&mut table_range_input).unwrap();
    table_range_input = table_range_input.strip_suffix("\n").unwrap().to_string();

    let table_range_split = table_range_input.split("-");
    let table_range_split = table_range_split.collect::<Vec<&str>>();

    let start = table_range_split[0].parse::<usize>().unwrap();
    let end = table_range_split[1].parse::<usize>().unwrap() + 1;

    println!("Times Table For {}, {}", times_table, table_range_input);

    for x in start..end {
        let result = times_table * x;
        println!("  {} x {} = {}", x, times_table, result);
    }
}
