class CliTimesTable {
    public static void main(String[] args) {
        System.out.print("Enter table number: ");
        String times_table_input = System.console().readLine();
        int times_table = Integer.parseInt(times_table_input);

        System.out.print("Enter range (e.g. 1-12): ");
        String table_range = System.console().readLine();
        String[] table_range_split = table_range.split("-", 2);

        int start = Integer.parseInt(table_range_split[0]);
        int end = Integer.parseInt(table_range_split[1]);

        end += 1;

        System.out.println(String.format("Times Table For %s, %s", times_table_input, table_range));

        for (int x = start; x < end; x++) {
            int result = times_table * x;
            System.out.println(String.format("  %d x %d = %d", x, times_table, result));
        }
    }
}
