# process_max_bet.py

def process_max_bet(table, starting_max, rounds, widths, roulette_option):
    previous_bet = 0
    running_loss = 0
    increment_bet = starting_max / (2 ** (rounds - 1))

    for i in range(1, rounds + 1):
        if i > 1:
            increment_bet = increment_bet * 2

        previous_bet = increment_bet
        profit = (increment_bet * 2) - running_loss - increment_bet
        running_loss = running_loss + previous_bet
        
        if (roulette_option == "euro"):
            prob_no_black = (1 - 19/37) ** i * 100
        else:
            prob_no_black = (1 - 18/38) ** i * 100

        max_bet_str = f"{starting_max if i == 1 else '' :<{widths[0]}}"
        round_str = f"{i:<{widths[1]}}"
        bet_str = f"{increment_bet:<{widths[2]}.2f}"
        profit_str = f"{profit:<{widths[3]}.2f}"
        running_loss_str = f"{running_loss:<{widths[4]}.2f}"
        prob_no_black_str = f"{prob_no_black:<{widths[5]}.2f}"

        table.append(f"| {max_bet_str} | {round_str} | {bet_str} | {profit_str} | {running_loss_str} | {prob_no_black_str} |\n")

    table.append("\n")
