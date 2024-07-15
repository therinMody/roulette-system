import random

# Run this script to run a simulation to confirm the debunking of the doubling down theory

"""
Allowed Max Bet: 500
|    Max Bet     |   Round    |       Bet       |   Profit - Running Loss   |     Running Loss     |  Euro Prob. No Black (%)  |  Amer. Prob. No Black (%) |
|----------------|------------|-----------------|---------------------------|----------------------|---------------------------|---------------------------|
| 500            | 1          | 0.98            | 0.98                      | 0.98                 | 51.35                     | 52.63                     |
|                | 2          | 1.95            | 0.98                      | 2.93                 | 26.37                     | 27.70                     |
|                | 3          | 3.91            | 0.98                      | 6.84                 | 13.54                     | 14.58                     |
|                | 4          | 7.81            | 0.98                      | 14.65                | 6.95                      | 7.67                      |
|                | 5          | 15.62           | 0.98                      | 30.27                | 3.57                      | 4.04                      |
|                | 6          | 31.25           | 0.98                      | 61.52                | 1.83                      | 2.13                      |
|                | 7          | 62.50           | 0.98                      | 124.02               | 0.94                      | 1.12                      |
|                | 8          | 125.00          | 0.98                      | 249.02               | 0.48                      | 0.59                      |
|                | 9          | 250.00          | 0.98                      | 499.02               | 0.25                      | 0.31                      |
|                | 10         | 500.00          | 0.98                      | 999.02               | 0.13                      | 0.16                      |

Probability of losing once before reaching Potential Running Loss: Euro: 73%, American: 81%
Games Necessary to win to cover a loss: 1023
"""

# Game scenarios
bet_amount = 1
max_bet = 500
rounds = 10
games_won_necessary = 1023
roulette_type = "euro"
initial_bank_roll = 1000

def play_round(roulette_type):
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

### WIP ###