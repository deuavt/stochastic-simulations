"""
Title: Roulette - Color vs Number Simulation

Description:
A Monte Carlo simulation plotting cumulative winnings for the following strategies on an American roulette wheel:
(a) Always betting on a color.
(b) Always betting on a number.
"""

from random import random, seed
import matplotlib.pyplot as plt

# Simulation settings.
BETS = 10 ** 4
# Random seed settings (int for set seed; None for random seed).
RAND_SEED = None

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

def trial_red(bets):
    """Simulate and plot cumulative winnings for color betting."""
    def bet():
        if random() < 18/38:
            return 1
        return -1
    yvalues = [0]
    # Simulate and plot `bets` bets.
    for i in range(bets):
        yvalues.append(yvalues[i]+bet())
    plot(range(1,bets+1), yvalues[1:], 'Color Betting')

def trial_num(bets):
    """Simulate and plot cumulative winnings for number betting."""
    def bet():
        if random() < 1/38:
            return 35
        return -1
    yvalues = [0]
    # Simulate and plot `bets` bets.
    for i in range(bets):
        yvalues.append(yvalues[i]+bet())
    plot(range(1,bets+1), yvalues[1:], 'Number Betting')

def main(bets, set_seed):
    """Perform, plot, and display simulations to the user."""
    # Apply randomizer seed if applicable.
    if set_seed is not None:
        seed(set_seed)
    # Run and display simulations to the user. 
    trial_red(bets)
    trial_num(bets)
    plt.legend()
    update_lims()
    plt.show()

if __name__ == "__main__":
    main(BETS, RAND_SEED)