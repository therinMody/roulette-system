# Roulette System Repository Overview

## Introduction

This document describes a systematic betting approach designed to optimize chances of achieving a net positive outcome. The strategy revolves around committing to a predefined number of rounds, with the necessity to stop immediately upon a win to prevent losses.

Each strategy has a new line for every betting round, the probability of losing. This takes into the account the amount of games you'd need to turn you initial investment into captial. Meaning if you invested $1000, what is more likely to happen; 1. Make a profit of $1000 or 2. Run into the low chance of striking out.

Say for example, we are playing a min outside bet of $1 with a max bet of $500. This accounts for 10 rounds of doubling. We would need to play 1023 games to win enough money to enter the green (money gained past our initial investment). Is it possible to win all these games without losing once? Yes. Are the odds in your favour? Not even close, terrible odds in fact.

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

After analyzing the contents of this repo, you'll know that this roulette strategy is to be avoided at all costs. Unless you run into a scenario without a max bet limit, in which case, make sure you have a massive bank roll to back you.

## Folder Structure

The `lib` directory contains various subdirectories named `round_x`, where `x` represents the number of rounds. Each folder contains a `README.md` file that outlines simulations for the respective number of rounds, showing detailed scenarios of bets and outcomes.

### Key Components

- **Max Bet**: The highest bet allowed.
- **Round**: Indicates the current round of betting.
- **Bet**: The actual bet placed.
- **Profit - Running Loss**: Shows the net outcome as the difference between profits and losses up to that round. 
- **Running Loss**: Cumulative losses over the rounds.
- **Game Won Necessary**: Games needed to win before encountering a single loss
- **Prob. of losing once**: Probability of losing while playing the required "Games Won Necessary" to enter the green

## Probability of Loss

A critical aspect of this strategy is the calculated probability of losing everything, a measure added to each round's summary to provide a statistical basis for the risk involved. This probability indicates how likely it is to lose all rounds, helping to manage expectations and strategy adherence. These numbers appeared to be very good at the start. The kicker comes in when you calculate how many games you'd need to play to cover one loss.

To cover one loss, we calculate the amount of games you'd need to win to equal one of these rare loss's. This equals the "Games Won Necessary" note after each table. Then we take the probability of losing (depends on the rounds and max bet) to the exponent of "Games Won Necessary". And the low chance of losing all n rounds, would turn out to happen to much over than expected, quite a bit more.

## Disclaimer

The betting strategy and the calculations provided herein are based on mathematical models and are intended for informational purposes only. Actual gambling involves risks, and this system, like any betting strategy, cannot guarantee profits. Users are advised to understand their financial and emotional capacity for risk before engaging in betting activities.

## Conclusion

This betting strategy has almost no upside. The high probability of losing at least once in the required number of "Games Won Necessary" far outweighs the potential for profit. Engaging in this strategy is likely to result in significant losses rather than gains.
