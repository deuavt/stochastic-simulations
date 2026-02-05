"""
Title: Roulette - Martingale Doubling System

Description:
A program plotting cumulative winnings for multiple Monte Carlo simulations of the Martingale Doubling System on an American roulette wheel.
"""

from random import random, seed
import matplotlib.pyplot as plt

# Simulation variables.
NUM_SIMS = 10**3
MAX_TRIALS = 10**3
# Random seed settings (int for set seed; None for random seed).
RAND_SEED = None

def plot(x, y, label=''):
    """Plot a set of x-y values with a legend label."""
    plt.plot(x, y, label=label)
    # Create x-axis.
    ax = plt.gca()
    ax.spines['bottom'].set_position(('data', 0)) 
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')

def update_lims(default=1, padding=0.05):
    """Set limits for plot to include all visible data."""
    ax = plt.gca()
    # Find the min and max y-values displayed in any given graph. 
    ymin = ymax = 0
    for line in ax.get_lines():
        ydata = line.get_ydata()
        ymin = min(ymin, ydata.min())
        ymax = max(ymax, ydata.max())
    # Apply limits with padding.
    pad = padding * (ymax - ymin or default)
    ax.set_ylim(ymin - pad, ymax + pad)

def martingale(max_trials):
    """Perform and plot a single simulation of the Martingale System until it succeeds or reaches `max_trials` trials."""
    # Initialise variables. 
    running_bet, profit_values = 1, [0]
    while len(profit_values) < max_trials + 1:
        # Simulate and record a single round using this system.
        if random() < 18/38:
            profit_values.append(profit_values[-1] + running_bet)
            break
        else:
            profit_values.append(profit_values[-1] - running_bet)
            running_bet *= 2
    plot(range(len(profit_values)), profit_values)

def main(num_sims, max_trials, set_seed):
    """Perform, plot, and display simulations to the user."""
    # Apply randomiser seed if applicable.
    if set_seed is not None:
        seed(set_seed)
    # Run `num_sims` Martingale Doubling trials and plot them.
    for trial in range(num_sims):
        martingale(max_trials)
    # Display plot to user.
    update_lims()
    plt.show()

if __name__ == "__main__":
    main(NUM_SIMS, MAX_TRIALS, RAND_SEED)