package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	fmt.Print("Enter table number: ")

	var times_table_input string
	fmt.Scanln(&times_table_input)

	times_table, _ := strconv.ParseUint(times_table_input, 10, 64)

	fmt.Print("Enter range (e.g. 1-12): ")
	var table_range string
	fmt.Scanln(&table_range)

	table_range_split := strings.Split(table_range, "-")

	start, _ := strconv.ParseUint(table_range_split[0], 10, 64)
	end, _ := strconv.ParseUint(table_range_split[1], 10, 64)

	end += 1

	fmt.Printf("Times Table For %d, %s:\n", times_table, table_range)

	for x := start; x < end; x++ {
		result := times_table * x
		fmt.Printf("  %d x %d = %d\n", x, times_table, result)
	}
}
