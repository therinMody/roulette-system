from . import process_max_bet
from . import headers

def readme_generator(rounds, destination):
    column_widths = [14, 10, 15, 25, 20, 20]  # Updated to include the new column for probability

    output_table = []
    max_bet_start = 500
    max_bet_limit = 10000
    increment = 500

    while max_bet_start <= max_bet_limit:
        output_table.append(f"Allowed Max Bet: {max_bet_start}\n")
        headers.headers(output_table, column_widths)  # Add header to table with defined widths
        process_max_bet.process_max_bet(output_table, max_bet_start, rounds, column_widths)  # Add rows to table
        output_table.append("\n\n")  # Add spacing between tables for different starting max bets
        max_bet_start += increment

    # Write the formatted table to README.md
    with open(destination, "w") as file:
        file.writelines(output_table)