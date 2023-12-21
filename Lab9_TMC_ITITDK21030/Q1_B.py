import numpy as np


def function_to_approximate(x):
    return x**2 * np.cos(x)


def central_difference_first_order(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


# Given values
x_value = 0.5
step_size = 0.1

# Compute the first-order central difference approximation
approximation = central_difference_first_order(
    function_to_approximate, x_value, step_size
)

# Print the result
print(
    f"The first-order central difference approximation at x = {x_value} with h = {step_size} is: {approximation}"
)
