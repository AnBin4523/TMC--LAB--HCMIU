import numpy as np

# Given data
x_values = np.array([0, 1, 2.5, 3, 4.5, 5, 6])
y_values = np.array([26, 15.5, 5.375, 3.5, 2.375, 3.5, 8])

# Function to calculate divided differences
def divided_differences(x, y):
    n = len(x)
    table = np.zeros((n, n))
    table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (x[i + j] - x[i])

    return table

# Newton interpolation function
def newton_interpolation(x, y, x_interpolate):
    result = y[0]

    for i in range(1, len(x)):
        term = 1
        for j in range(i):
            term *= (x_interpolate - x[j])
        result += term * divided_diff_table[0, i]

    return result

# Calculate divided differences
divided_diff_table = divided_differences(x_values, y_values)

# Calculate y at x = 3.5 using Newton interpolation
x_interpolate = 3.5
y_interpolated = newton_interpolation(x_values, y_values, x_interpolate)

# Print the result
print(f"The interpolated value at x = {x_interpolate} is exactly {y_interpolated:.6f}")
