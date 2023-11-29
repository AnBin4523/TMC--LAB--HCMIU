#Ngo Le Thien An - ITITDK21030
#Q3

import random

# Define the function to maximize
def f(x, y):
    return 3.5 * x + 2 * y + x**2 - x**4 - 2 * x * y - y**2

# Range for x and y
x_range = (-2, 2)
y_range = (-2, 2)

# Number of random samples
num_samples = 1000

# Initialize variables to store the maximum and corresponding point
max_value = -float('inf')
max_point = None

# Perform random search
for _ in range(num_samples):
    x = random.uniform(x_range[0], x_range[1])
    y = random.uniform(y_range[0], y_range[1])
    value = f(x, y)
    
    if value > max_value:
        max_value = value
        max_point = (x, y)

# Maximum point and value
print("Estimated Maximum:")
print(f"x = {max_point[0]:.4f}")
print(f"y = {max_point[1]:.4f}")
print(f"f(x, y) = {max_value:.4f}")
