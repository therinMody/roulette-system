def headers(table, widths):
    header_titles = ["Max Bet", "Round", "Bet", "Profit - Running Loss", "Running Loss", "Euro Prob. No Black (%)", "Amer. Prob. No Black (%)"]
    
    # Create the header row
    header_row = '|'
    separator_row = '|'
    for index, title in enumerate(header_titles):
        header_row += f" {title.center(widths[index])} |"
        separator_row += '-' * (widths[index] + 2) + '|'
    
    # Append rows to the table list
    table.append(header_row + '\n')
    table.append(separator_row + '\n')