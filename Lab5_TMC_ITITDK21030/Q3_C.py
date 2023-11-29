#Ngo Le Thien An - ITITDK21030
import numpy as np
from scipy.optimize import linprog

# Objective function coefficients
c = [-45, -20, 0, 0, 0]

# Coefficients matrix for constraints
A = np.array([
    [20, 5, 1, 0, 0],    # Raw Material Constraint
    [0.04, 0.12, 0, 1, 0],    # Production Time Constraint
    [1, 1, 0, 0, 1]    # Storage Capacity Constraint
])

# RHS values
b = [9500, 40, 550]

# Variable bounds (x and y should be non-negative by default)
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds, (0, None), (0, None), (0, None)])

# Extract and print the results
if result.success:
    print("Optimal Solution:")
    x_optimal, y_optimal = result.x[0], result.x[1]
    optimal_profit = -result.fun  # Negative sign because linprog minimizes by default
    print(f"x (Product A) = {x_optimal:.2f}")
    print(f"y (Product B) = {y_optimal:.2f}")
    print(f"Optimal Profit = ${optimal_profit:.2f}")
else:
    print("No optimal solution found.")
