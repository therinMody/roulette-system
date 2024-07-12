# headers.py

def headers(table, widths):
    header_titles = ["Max Bet", "Round", "Bet", "Profit - Running Loss", "Running Loss", "Prob. No Black (%)"]
    header_underlines = [""] * len(header_titles)  # Create an empty list for underlines

    # Generate headers with specific widths
    for index, title in enumerate(header_titles):
        header_underlines[index] = "-" * widths[index]  # Underlines
        table.append(f"| {title.center(widths[index])} ")  # Center align title within its width

    table.append("|\n")  # End of header row
    table.append("+")  # Start the bottom line of the header

    # Generate the bottom line of the header
    for width in widths:
        table.append("-" * (width + 2) + "+")  # "+2" accounts for padding spaces around the text

    table.append("\n")
