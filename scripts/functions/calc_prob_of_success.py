import math

def calc_prob_of_success(rounds, profit, running_loss):
    
    # Games
    games_needed_for_cover = running_loss / profit
    
    # P(Loss)
    euro_prob_loss = (19 / 37) ** rounds
    amer_prob_loss = (20 / 38) ** rounds
    
    # P(Win) = 1 - P(Lose)
    euro_prob_win = 1 - euro_prob_loss
    amer_prob_win = 1 - amer_prob_loss
    
    # P(Win all) = (P(Win))^Games
    euro_prob_win_all = euro_prob_win ** games_needed_for_cover
    amer_prob_win_all = amer_prob_win ** games_needed_for_cover
    
    # P(Lose at least once) = 1 - P(Win all)
    euro_prob_one_loss = 1 - euro_prob_win_all
    amer_prob_one_loss = 1 - amer_prob_win_all
    
    euro_prob_one_loss_percent = round(euro_prob_one_loss * 100)
    amer_prob_one_loss_percent = round(amer_prob_one_loss * 100)
    
    return math.ceil(games_needed_for_cover), euro_prob_one_loss_percent, amer_prob_one_loss_percent