import numpy as np
import matplotlib.pyplot as plt

# Data
rounds = 3129
ops = 6.1634  # Operations per second (Kops/s)

# Let's create a simple dataset where we assume different rounds for testing
# We'll assume that as the number of rounds increases, OPS might change linearly for the sake of the example
rounds_values = np.array([1000, 1500, 2000, 2500, 3000, 3500])  # Sample sizes (rounds)
ops_values = np.array([4.5, 5.2, 5.8, 6.1, 6.3, 6.5])  # OPS corresponding to those rounds

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(rounds_values, ops_values, marker='o', linestyle='-', color='b', label="Computing Effort (OPS)")

# Highlight the provided data point
plt.scatter(rounds, ops, color='red', zorder=5, label=f"Test Data (Rounds: {rounds}, OPS: {ops})")

# Add labels and title
plt.title('Computing Effort vs Sample Size O(n^3)', fontsize=14)
plt.xlabel('Sample Size (Rounds)', fontsize=12)
plt.ylabel('Computing Effort (OPS - Kops/s)', fontsize=12)

# Add grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()