#Ngo Le Thien An - ITITDK21030
import numpy as np

# Define the function f(x, y)
def f(x, y):
    return -9 * x + x**2 + 11 * y + 4 * y**2 - 2 * x * y

# Calculate the gradient of the function
def gradient(x, y):
    df_dx = 2 * x - 9 - 2 * y
    df_dy = 11 + 8 * y - 2 * x
    return np.array([df_dx, df_dy])

# Calculate the Hessian matrix
def hessian(x, y):
    df2_dx2 = 2
    df2_dxdy = -2
    df2_dy2 = 8
    return np.array([[df2_dx2, df2_dxdy], [df2_dxdy, df2_dy2]])

# Perform Newton's method
def newton_optimization(initial_guess, alpha, num_iterations):
    x, y = initial_guess
    history = []  # To store the function values at each iteration

    for _ in range(num_iterations):
        grad = gradient(x, y)
        hess_inv = np.linalg.inv(hessian(x, y))
        direction = np.dot(hess_inv, grad)
        x -= alpha * direction[0]
        y -= alpha * direction[1]
        value = f(x, y)
        history.append(value)
        print(f"f({x:.4f}, {y:.4f}) = {value:.4f}")

    return history

# Initial guesses
initial_guess = [0, 0]

# Step size (adjust as needed)
alpha = 1

# Number of iterations
num_iterations = 5

# Perform Newton's method
history = newton_optimization(initial_guess, alpha, num_iterations)
