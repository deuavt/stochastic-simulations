"""
Title: Roulette - Color vs Number Simulation

Description:
A Monte Carlo simulation plotting cumulative winnings for the following strategies on an American roulette wheel:
(a) Always betting on a color.
(b) Always betting on a number.
"""

from random import random
import matplotlib.pyplot as plt
import numpy as np

def plot(x, y, label):
    """Plot a set of x-y values with a legend label."""
    x, y = np.array(x), np.array(y)
    plt.plot(x, y, label=label)
    # Create x-axis.
    ax = plt.gca()
    ax.spines['bottom'].set_position(('data', 0)) 
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    # Set y-limits to be equal distance from the x-axis.
    ymin, ymax = ax.get_ylim()
    M = max(abs(y.min()), abs(y.max()), abs(ymin), abs(ymax))
    ax.set_ylim(-M, M)

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

def run(bets):
    """Perform, plot, and display simulations to the user."""
    trial_red(bets)
    trial_num(bets)
    plt.legend()
    plt.show()

# Number of bets to simulate.
bets=10000

run(bets)
