import random

def play_game(roulette_type):
    """
    Simulates a single round of betting on black in roulette.
    
    Parameters:
    - roulette_type: A string that specifies the type of roulette ("euro" for European, "amer" for American).
    
    Returns:
    - 1 if the bet wins (lands on black)
    - 0 if the bet loses (lands on red or green)
    """
    if roulette_type == "amer":
        # American roulette: 18 black, 18 red, 2 green
        outcome = random.randint(1, 38)  # 1-18: black, 19-36: red, 37-38: green
        if outcome <= 18:
            return 1
        else:
            return 0
    elif roulette_type == "euro":
        # European roulette: 18 black, 18 red, 1 green
        outcome = random.randint(1, 37)  # 1-18: black, 19-36: red, 37: green
        if outcome <= 18:
            return 1
        else:
            return 0
    else:
        raise ValueError("Invalid roulette type. Use 'euro' for European or 'amer' for American.")

def play_rounds(roulette_type, rounds):
    """
    Simulates multiple rounds of roulette, stopping if a win is achieved.
    
    Parameters:
    - roulette_type: A string that specifies the type of roulette ("euro" for European, "amer" for American).
    - rounds: The number of rounds to play.
    
    Returns:
    - 1 if a win is achieved before the rounds are exhausted
    - 0 if no win is achieved within the given rounds
    """
    for i in range(1, rounds + 1):
        # Play a single game
        result = play_game(roulette_type)
        
        # Check if we won the game
        if result == 1:
            break

    # Check if we lost all rounds without winning
    if i == rounds:
        return 0
    else:
        return 1

def play_for_profit(roulette_type, rounds, games_won_necessary):
    """
    Simulates the process of trying to win a certain number of games in multiple rounds.
    
    Parameters:
    - roulette_type: A string that specifies the type of roulette ("euro" for European, "amer" for American).
    - rounds: The number of rounds to play in each game.
    - games_won_necessary: The number of games that need to be won to achieve a profit.
    
    Returns:
    - 1 if the necessary number of games are won before encountering a loss
    - 0 if a loss is encountered before reaching the necessary number of wins
    """
    for i in range(1, games_won_necessary + 1):
        if play_rounds(roulette_type, rounds) == 0:
            return 0 # We encountered a loss
    return 1 # We made it to the necessary number of wins before losing

def run_simulation(trys, roulette_type, rounds, games_won_necessary_for_profit):
    wins = 0
    losses = 0

    for i in range(1, trys + 1):
        result = play_for_profit(roulette_type, rounds, games_won_necessary_for_profit)
        if result == 1:
            wins += 1
        else:
            losses += 1

    return wins, losses