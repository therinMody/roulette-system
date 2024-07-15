# process_max_bet.py
from . import calc_prob_of_success

def process_max_bet(table, starting_max, rounds, widths):
    previous_bet = 0
    running_loss = 0
    increment_bet = starting_max / (2 ** (rounds - 1))

    for i in range(1, rounds + 1):
        if i > 1:
            increment_bet = increment_bet * 2

        previous_bet = increment_bet
        profit = (increment_bet * 2) - running_loss - increment_bet
        running_loss = running_loss + previous_bet
        
        euro_prob_no_black = (1 - 18/37) ** i * 100
        amer_prob_no_black = (1 - 18/38) ** i * 100

        max_bet_str = f"{starting_max if i == 1 else '' :<{widths[0]}}"
        round_str = f"{i:<{widths[1]}}"
        bet_str = f"{increment_bet:<{widths[2]}.2f}"
        profit_str = f"{profit:<{widths[3]}.2f}"
        running_loss_str = f"{running_loss:<{widths[4]}.2f}"
        euro_prob_no_black_str = f"{euro_prob_no_black:<{widths[5]}.2f}"
        amer_prob_no_black_str = f"{amer_prob_no_black:<{widths[6]}.2f}"

        table.append(f"| {max_bet_str} | {round_str} | {bet_str} | {profit_str} | {running_loss_str} | {euro_prob_no_black_str} | {amer_prob_no_black_str} |\n")

    table.append("\n")
    
    return calc_prob_of_success.calc_prob_of_success(rounds, profit, running_loss)
