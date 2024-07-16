from functions.play import play_for_profit
import time

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

# Needs a math check
 
def main():
    # Game scenarios
    rounds = 10
    games_won_necessary_for_profit = 1023
    roulette_type = "euro"
    
    # How many times would you like to try to turn a profit?
    trys = 1000000
    
    print(f"-------------------------- Running Simulation of {trys} attempts --------------------------")
    wins = 0
    losses = 0

    for i in range(1, trys + 1):
        result = play_for_profit(roulette_type, rounds, games_won_necessary_for_profit)
        if result == 1:
            print(f"Try {i:<3} : Congrats, you won {games_won_necessary_for_profit} in a row to turn a profit")
            wins += 1
        else:
            print(f"Try {i:<3} : You lost before turning your investment into capital")
            losses += 1

    print(f"------------------------------------- End Simulation ----------------------------------")
    
    if wins > losses:
        # Likely never going to see this print statement
        print(f"Overall: You won {(wins/trys) * 100}% of the games")
    else:
        print(f"Overall: You lost {(losses/trys) * 100}% of the games")
    
if __name__ == '__main__':
    # Start the timer
    start_time = time.time()
    main()
    # End the timer
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    print(f"Time taken to run the simulation: {elapsed_time:.2f} seconds")
