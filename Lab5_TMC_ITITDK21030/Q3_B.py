#Ngo Le Thien An - ITITDK21030
import matplotlib.pyplot as plt
import numpy as np

# Define the constraints
x = np.linspace(0, 600, 400)
y1 = -4 * x + 1900
y2 = -1/3 * x + 1000/3
y3 = -x + 550

# Plot the constraints
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='20x + 5y ≤ 9500')
plt.plot(x, y2, label='0.04x + 0.12y ≤ 40')
plt.plot(x, y3, label='x + y ≤ 550')

# Fill the feasible region
plt.fill_between(x, 0, np.minimum(np.minimum(y1, y2), y3), where=(0 <= x) & (x <= 600), color='gray', alpha=0.5)

# Set non-negativity constraints
plt.xlim(0, 600)
plt.ylim(0, 600)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Label axes and constraints
plt.xlabel('x (Product A)')
plt.ylabel('y (Product B)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
