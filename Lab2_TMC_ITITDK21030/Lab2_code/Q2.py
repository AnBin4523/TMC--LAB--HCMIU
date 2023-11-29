import math

# Define the function
def f(x):
    return -2 * x**6 - 1.6 * x**4 + 12 * x + 1

# Define the initial guesses
x1 = 0.0
x2 = 1.0

# Define the desired relative error threshold
desired_relative_error = 0.05

# Initialize relative error
relative_error = 1.0 

# Perform the bisection method
while relative_error >= desired_relative_error:
    # Calculate the midpoint
    c = (x1 + x2) / 2

    # Evaluate function values at x1, x2, and c
    f1 = f(x1)
    f2 = f(x2)
    fc = f(c)

    # Check the sign of fc
    if fc > 0:
        x2 = c
    elif fc < 0:
        x1 = c
    else:
        break  # If fc is exactly 0, stop because we've found the maximum

    # Handle the case where x2 and x1 become equal
    if x2 == x1:
        break

    # Calculate relative error
    relative_error = abs(x2 - x1) / x2 if x2 != 0 else abs(x2 - x1)

# Calculate the approximate maximum value
maximum_value = f(c)

# Print the results
print("Approximate Maximum Value:", maximum_value)
print("Approximate Relative Error:", relative_error)
