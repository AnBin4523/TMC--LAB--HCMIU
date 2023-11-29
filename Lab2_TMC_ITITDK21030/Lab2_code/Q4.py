def f(x):
    return x**3.5 - 80

# Define initial guesses
x1 = 2.0
x2 = 5.0

# Define the desired relative error
desired_relative_error = 0.025  # 2.5% as a decimal

# Initialize relative error
relative_error = 1.0  # A value greater than the threshold to start the loop

# Perform the false-position method
while relative_error >= desired_relative_error:
    # Calculate the new approximation using false-position formula
    x_new = (x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))

    # Evaluate the function at the new approximation
    f_new = f(x_new)

    # Update x1 or x2 based on the sign of f_new
    if f_new > 0:
        x1 = x_new
    elif f_new < 0:
        x2 = x_new
    else:
        break  # If f_new is exactly 0, stop because we've found the root

    # Calculate relative error
    relative_error = abs(x2 - x1) / x2 if x2 != 0 else abs(x2 - x1)

# Print the result
print("Approximate Root using False-Position Method:", x_new)
print("Approximate Relative Error:", relative_error)
