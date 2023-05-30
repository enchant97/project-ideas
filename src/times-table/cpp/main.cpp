//
// CLI Times Table C++ Solution
// Author: Leo Spratt
// SPDX-License-Identifier: MIT
//

#include <iostream>
#include <string>

int main() {
    int times_table;
    std::string table_range;
    std::string start_str;
    std::string end_str;
    int start;
    int end;

    std::cout << "Enter table number: ";
    std::cin >> times_table;

    std::cout << "Enter range (e.g. 1-12): ";
    std::cin >> table_range;

    start_str = table_range.substr(
        0,
        table_range.find("-")
    );
    start = std::stoi(start_str);

    end_str = table_range.substr(
        table_range.find("-") + 1,
        table_range.length()
    );
    end = std::stoi(end_str) + 1;

    std::cout << "Times Table for " << table_range << ":" << std::endl;

    for (int x = start; x < end; x++) {
        int result = times_table * x;
        std::cout << x << " x " << times_table << " = " << result << std::endl;
    }

    return 0;
}
