"""
Title: Monte Carlo Pi Approximator 

Description:
A Monte Carlo simulation using the uniform distribution on the unit square to:
(a) Estimate the area of the circle of radius 1/2 centered at (1/2, 1/2).
(b) Approximate pi using this area (A = pi * r^2 -> pi = A/r^2 = 4A).
(c) Show this process visually throughout the simulation.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Simulation settings.
BATCH_SIZE = 10**4
MAX_POINTS = 10**6
UPDATE_INTERVAL = 100 # (ms)
# Visual settings.
POINT_TRANSPARENCY = 0.025
CIRCLE_COLOR = "black"
POINT_COLOR = "red"
# Random seed settings (int for set seed; None for random seed).
RAND_SEED = None

def main():
    """Perform and display simulation using matplotlib."""
    # Initialize numerical variables.
    count = count_in = 0
    points = np.empty((MAX_POINTS, 2))
    # Define center constant to be used in calculation.
    center = np.array([1/2, 1/2])

    # Initialize randomization using seed if supplied.
    np.random.seed(RAND_SEED)

    # Matplotlib setup.
    fig, ax = plt.subplots()
    fig.suptitle("Visual π Approximator")
    fig.canvas.manager.set_window_title("Visual π Approximator")

    # Initialize animated variables.
    approx_text = fig.text(0.15, 0.9, "")
    points_scat = ax.scatter([], [], s=1, color=POINT_COLOR, alpha=POINT_TRANSPARENCY)

    # Plot a circle centered at (1/2, 1/2) with radius 1/2.
    x = np.linspace(0, 1, 50)
    y1 = np.sqrt((1/2)**2 - (x - 1/2)**2) + 1/2
    y2 = -y1 + 1

    ax.plot(x, y1, color=CIRCLE_COLOR)
    ax.plot(x, y2, color=CIRCLE_COLOR)

    # Set axes limits.
    ax.set(xlim=(0, 1), ylim=(0, 1))

    # Initialization function for mpl animation.
    def init():
        approx_text.set_text("pi ≈ ...")
        points_scat.set_offsets(np.empty((0, 2)))
        return (approx_text, points_scat)

    # Update function for mpl animation.
    def update(frame):
        """Generate a new batch of points, updating the approximation and plot."""
        # Make nonlocal to allow in-function updating.
        nonlocal count, count_in

        # Calculate the number of points to generate. 
        to_gen = min(MAX_POINTS - count, BATCH_SIZE)
        if to_gen <= 0:
            return (approx_text, points_scat)

        # Generate batch of points randomly in the unit square.
        batch = np.random.rand(to_gen, 2)
        # Count those in the batch inside the plotted circle.
        squared_dists = np.sum((batch - center)**2, axis=1)
        count_in += np.count_nonzero(squared_dists < 1/4)
        # Update the total points generated.
        count += to_gen
        # Append the new batch to the graphed points.
        points[count-to_gen:count] = batch
        points_scat.set_offsets(points[:count])
    
        # Approximate the area of the circle using the law of large numbers on the uniform distribution.
        approx_area = count_in/count
        # Approximate pi with this area via. A = pi * r^2 -> pi = 4A.
        approx_num = 4 * approx_area
        # Update the displayed approximation.
        approx_text.set_text(f"pi ≈ {approx_num:.7f}")
        
        return (approx_text, points_scat)

    # Calculate the number of updates needed to complete the simulation.
    updates = MAX_POINTS//BATCH_SIZE 
    if MAX_POINTS % BATCH_SIZE != 0:
        updates += 1

    # Define the animation.
    # blit = False to allow the animated text to be drawn in the fig environment.
    ani = FuncAnimation(fig, update, frames=updates, init_func=init, interval=UPDATE_INTERVAL, blit=False)
    
    # Initialize the plot, starting the simulation.
    plt.show()

if __name__ == "__main__":
    main()
