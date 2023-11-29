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

# Solve the problem to obtain the optimal solution
problem.solve()

if problem.status == cp.OPTIMAL:
    # Calculate and print the shadow prices (dual values)
    shadow_price_raw_material = constraints[0].dual_value
    shadow_price_production_time = constraints[1].dual_value
    shadow_price_storage_capacity = constraints[2].dual_value
    
    print(f"Shadow Price (Raw Material): ${shadow_price_raw_material:.2f} per kg")
    print(f"Shadow Price (Production Time): ${shadow_price_production_time:.2f} per hour")
    print(f"Shadow Price (Storage Capacity): ${shadow_price_storage_capacity:.2f} per unit of storage")

    # Determine which option raises profits the most based on the signs of shadow prices
    if shadow_price_raw_material > 0:
        print("Increasing raw material will raise profits.")
    if shadow_price_production_time > 0:
        print("Increasing production time will raise profits.")
    if shadow_price_storage_capacity > 0:
        print("Increasing storage capacity will raise profits.")
else:
    print("No optimal solution found.")
