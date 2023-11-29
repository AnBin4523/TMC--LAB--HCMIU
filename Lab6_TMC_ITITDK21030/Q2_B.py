#Ngo Le Thien An
#Q2_B

import numpy as np
import matplotlib.pyplot as plt

# Define the function to maximize
def f(x, y):
    return 3.5 * x + 2 * y + x**2 - x**4 + 2 * x * y - y**2

# Calculate the gradient numerically using the central difference method
def gradient(f, x, y, h=1e-4):
    df_dx = (f(x + h, y) - f(x - h, y)) / (2 * h)
    df_dy = (f(x, y + h) - f(x, y - h)) / (2 * h)
    return df_dx, df_dy

# Gradient ascent method
def gradient_ascent(f, x0, y0, step_size, num_iterations):
    x_values = [x0]
    y_values = [y0]
    function_values = [f(x0, y0)]

    for _ in range(num_iterations):
        df_dx, df_dy = gradient(f, x_values[-1], y_values[-1])
        x_values.append(x_values[-1] + step_size * df_dx)
        y_values.append(y_values[-1] + step_size * df_dy)
        function_values.append(f(x_values[-1], y_values[-1]))

    return x_values, y_values, function_values

# Different step sizes to test
step_sizes = [0.01, 0.1, 0.5, 1]
num_iterations = 50

plt.figure(figsize=(12, 6))

for step_size in step_sizes:
    x_values, y_values, function_values = gradient_ascent(f, 0, 0, step_size, num_iterations)
    plt.plot(range(num_iterations + 1), function_values, label=f"Step Size = {step_size}")

plt.xlabel("Iterations")
plt.ylabel("Function Value")
plt.title("Gradient Ascent Convergence with Different Step Sizes")
plt.legend()
plt.grid(True)
plt.show()