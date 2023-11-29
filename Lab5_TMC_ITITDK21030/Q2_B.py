#Ngo Le Thien An - ITITDK21030
import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x, y)
def f(x, y):
    return -9 * x + x**2 + 11 * y + 4 * y**2 - 2 * x * y

# Numerical gradient calculation using central difference method
def numerical_gradient(x, y, h):
    df_dx = (f(x + h, y) - f(x - h, y)) / (2 * h)
    df_dy = (f(x, y + h) - f(x, y - h)) / (2 * h)
    return df_dx, df_dy

# Gradient descent method
def gradient_descent(learning_rate, num_iterations):
    x, y = 0, 0  # Initial guesses
    history = []  # To store the function values at each iteration

    for iteration in range(num_iterations):
        gradient_x, gradient_y = numerical_gradient(x, y, 1e-5)  # Numerical gradient
        x -= learning_rate * gradient_x
        y -= learning_rate * gradient_y
        value = f(x, y)
        history.append(value)
        print(f"Iteration {iteration + 1}: f({x:.4f}, {y:.4f}) = {value:.4f}")

    return history

# List of different step sizes
learning_rates = [0.01, 0.1, 0.5, 1]

# Number of iterations
num_iterations = 50

# Perform gradient descent with different step sizes and store results
results = {}
for lr in learning_rates:
    history = gradient_descent(lr, num_iterations)
    results[lr] = history

# Plot the value of the function versus iterations for each step size
plt.figure(figsize=(10, 6))
for lr in learning_rates:
    plt.plot(range(num_iterations), results[lr], label=f"Step Size {lr}")
plt.xlabel("Iterations")
plt.ylabel("f(x, y)")
plt.title("Convergence Rates of Gradient Descent with Different Step Sizes")
plt.legend()
plt.show()
