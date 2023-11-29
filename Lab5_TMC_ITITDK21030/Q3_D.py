#Ngo Le Thien An - ITITDK21030
import cvxpy as cp

# Define the decision variables
x = cp.Variable()
y = cp.Variable()

# Define the objective function to maximize
objective = cp.Maximize(45 * x + 20 * y)

# Define the constraints
constraints = [
    20 * x + 5 * y <= 9500,  # Raw Material Constraint
    0.04 * x + 0.12 * y <= 40,  # Production Time Constraint
    x + y <= 550,  # Storage Capacity Constraint
    x >= 0,  # Non-Negativity Constraint for x
    y >= 0,  # Non-Negativity Constraint for y
]

# Create the linear programming problem
problem = cp.Problem(objective, constraints)

# Solve the problem
problem.solve()

# Print the results
if problem.status == cp.OPTIMAL:
    print("Optimal Solution:")
    print(f"x (Product A) = {x.value:.2f}")
    print(f"y (Product B) = {y.value:.2f}")
    print(f"Optimal Profit = ${problem.value:.2f}")
else:
    print("No optimal solution found.")
