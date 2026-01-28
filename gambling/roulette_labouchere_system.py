"""
Title: Roulette - Labouchere System

Description:
A program plotting cumulative winnings for multiple Monte Carlo simulations of the Labouchere System on an American roulette wheel.
"""

from random import random, seed
import matplotlib.pyplot as plt

def plot(x, y, label = ''):
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

def labouchere(start_list, max_trials):
    """Perform and plot a single simulation of the Labouchere System until it succeeds or reaches `max_trials` trials."""
    # Initialise lists
    running_list, profit_values = list(start_list), [0]
    while running_list and len(profit_values) < max_trials + 1:
        # Calculate this rounds bet.
        bet = running_list[0]
        if len(running_list) != 1:
            bet += running_list[-1]
        # Simulate and record a single round using this system.
        if random() < 18/38:
            # Remove trailing elements (which sum to the money won) in the case of a win.
            del running_list[0]
            if running_list:
                del running_list[-1]
            profit_values.append(profit_values[-1] + bet)
        else:
            # Append the money lost in the case of a loss.
            running_list.append(bet)
            profit_values.append(profit_values[-1] - bet)
    plot(range(len(profit_values)), profit_values)

def run(start_list, num_trials, max_trials, set_seed=None):
    """Perform, plot, and display simulations to the user."""
    # Apply randomiser seed if applicable.
    if set_seed is not None:
        seed(set_seed)
    # Run `num_trials` Labouchere trials and plot them.
    for trial in range(num_trials):
        labouchere(start_list, max_trials)
    # Display plot to user.
    update_lims()
    plt.show()

# Simulation variables.
start_list = (1, 2, 3, 4)
num_trials = 1000
max_trials = 500

run(start_list, num_trials, max_trials, set_seed=123)