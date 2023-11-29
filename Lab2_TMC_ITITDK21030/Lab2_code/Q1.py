import math
import matplotlib.pyplot as plt

# Define the function to find the root of
def f(x):
    return math.log(x**4) - 0.7

# Define initial guesses for bisection and false-position methods
x1_bisection = 0.5
x2_bisection = 2.0
x1_false_position = 0.5
x2_false_position = 2.0

# Define the desired relative error (assuming 3 iterations)
desired_relative_error = 0.025  # 2.5% as a decimal

# Initialize relative error for both methods
relative_error_bisection = 1.0  # A value greater than the threshold to start the loop
relative_error_false_position = 1.0

# Lists to store the iterations for bisection and false-position methods
bisection_iterations = []
false_position_iterations = []

# Perform graphical method (plot the function)
x_values = [0.001 + 0.001 * i for i in range(1000)]  # Generate x values
y_values = [f(x) for x in x_values]  # Calculate corresponding y values
plt.plot(x_values, y_values, label='ln(x^4) - 0.7')

# Graphical method: Find the positive real root visually
plt.axhline(0, color='red', linestyle='--', label='y=0')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graphical Method')
plt.legend()
plt.grid(True)
plt.show()

# Bisection method
for i in range(3):  # Perform 3 iterations
    # Calculate the new approximation using the bisection formula
    x_bisection = (x1_bisection + x2_bisection) / 2

    # Evaluate the function at the new approximation
    f_bisection = f(x_bisection)

    # Update x1 or x2 based on the sign of f_bisection
    if f_bisection > 0:
        x2_bisection = x_bisection
    elif f_bisection < 0:
        x1_bisection = x_bisection
    else:
        break  # If f_bisection is exactly 0, stop because we've found the root

    # Calculate relative error for bisection method
    relative_error_bisection = abs(x2_bisection - x1_bisection) / x2_bisection if x2_bisection != 0 else abs(x2_bisection - x1_bisection)
    bisection_iterations.append((i+1, x_bisection, relative_error_bisection))

# False-position method
for i in range(3):  # Perform 3 iterations
    # Calculate function values at x1 and x2
    f1 = f(x1_false_position)
    f2 = f(x2_false_position)

    # Calculate the new approximation using the false-position formula
    x_new_false_position = x2_false_position - (f2 * (x2_false_position - x1_false_position)) / (f2 - f1)

    # Evaluate the function at the new approximation
    f_new_false_position = f(x_new_false_position)

    # Update x1 or x2 based on the sign of f_new_false_position
    if f_new_false_position > 0:
        x2_false_position = x_new_false_position
    elif f_new_false_position < 0:
        x1_false_position = x_new_false_position
    else:
        break  # If f_new_false_position is exactly 0, stop because we've found the root

    # Calculate relative error for false-position method
    relative_error_false_position = abs(x2_false_position - x1_false_position) / x2_false_position if x2_false_position != 0 else abs(x2_false_position - x1_false_position)
    false_position_iterations.append((i+1, x_new_false_position, relative_error_false_position))

# Print the results
print("Bisection Method Iterations:")
print("Iteration | x | Relative Error")
for iteration in bisection_iterations:
    print(iteration[0], '|', iteration[1], '|', iteration[2])

print("\nFalse-Position Method Iterations:")
print("Iteration | x | Relative Error")
for iteration in false_position_iterations:
    print(iteration[0], '|', iteration[1], '|', iteration[2])
