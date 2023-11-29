#Ngo Le Thien An - ITITDK21030
#Q2_D

import numpy as np

# Define the function to maximize
def f(x, y):
    return 3.5 * x + 2 * y + x**2 - x**4 + 2 * x * y - y**2

# Calculate the gradient vector of the function
def gradient(x, y):
    df_dx = 3.5 + 2 * x + 2 * y - 4 * x**3
    df_dy = 2 - 2 * y + 2 * x
    return np.array([df_dx, df_dy])

# Calculate the Hessian matrix of the function
def hessian(x, y):
    d2f_dx2 = 2 - 12 * x**2
    d2f_dy2 = -2
    d2f_dxdy = 2
    return np.array([[d2f_dx2, d2f_dxdy], [d2f_dxdy, d2f_dy2]])

# Initialize the point (x, y)
x = 0.0
y = 0.0

# Maximum number of iterations
max_iterations = 100

# Convergence criteria
tolerance = 1e-6

for iteration in range(max_iterations):
    grad = gradient(x, y)
    hess = hessian(x, y)
    
    # Calculate the search direction using the inverse Hessian
    search_direction = -np.linalg.solve(hess, grad)
    
    # Update the point (x, y)
    x += search_direction[0]
    y += search_direction[1]
    
    # Check for convergence
    if np.linalg.norm(search_direction) < tolerance:
        break

# Updated point is the estimate of the maximum
print("Estimated Maximum:")
print(f"x = {x:.4f}")
print(f"y = {y:.4f}")
print(f"Maximum at f(x, y) = {f(x, y):.4f}")
