#Ngo Le Thien An - ITITDK21030
#Q1_A

import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 2, 100)
x2_constraint = 2 - 2 * x1  # Rearranging the first constraint

# Plot the feasible region
plt.plot(x1, x2_constraint, label="2x1 + x2 ≤ 2")
plt.fill_between(x1, 0, x2_constraint, where=(x1 >= 0) & (x2_constraint >= 0), alpha=0.3, color='gray', label="Feasible Region")

# Set the x and y axis labels
plt.xlabel("x1")
plt.ylabel("x2")

# Set the x and y axis limits
plt.xlim(0, 2)
plt.ylim(0, 2)

# Add labels for the constraints
plt.text(0.5, 1.2, "2x1 + x2 ≤ 2", ha="center")
plt.text(0.2, 0.1, "x1 ≥ 0", ha="center")
plt.text(1.2, 0.1, "x2 ≥ 0", ha="center")

# Show the plot
plt.legend()
plt.grid(True)
plt.show()