import numpy as np
import matplotlib.pyplot as plt

# Given data
time = np.array([0, 25, 50, 75, 100, 125])  # in seconds
distance = np.array([0, 32, 58, 78, 92, 100])  # in kilometers

# Function to compute numerical derivatives
def numerical_derivative(x, y):
    h = x[1] - x[0]  # Assuming uniform spacing
    velocity = np.gradient(y, h)
    acceleration = np.gradient(velocity, h)
    return velocity, acceleration

# Compute numerical derivatives
velocity, acceleration = numerical_derivative(time, distance)

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(time, velocity, marker='o', linestyle='-', color='b')
plt.title('Rocket Velocity vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (km/s)')

plt.subplot(2, 1, 2)
plt.plot(time, acceleration, marker='o', linestyle='-', color='r')
plt.title('Rocket Acceleration vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (km/s^2)')

plt.tight_layout()
plt.show()
