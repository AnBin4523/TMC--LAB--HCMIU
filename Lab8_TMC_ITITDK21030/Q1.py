import numpy as np

# Given data
t_values = np.array([2, 2.1, 2.2, 2.7, 3, 3.4])
z_values = np.array([6, 7.752, 10.256, 36.576, 66, 125.168])

# Function to calculate divided differences
def divided_differences(t, z):
    n = len(t)
    table = np.zeros((n, n))
    table[:, 0] = z

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (t[i + j] - t[i])

    return table

# Newton interpolation function
def newton_interpolation(t, z, x):
    n = len(t)
    result = z[0]

    for i in range(1, n):
        term = 1
        for j in range(i):
            term *= (x - t[j])
        result += term * divided_diff_table[0, i]

    return result

# Calculate divided differences
divided_diff_table = divided_differences(t_values, z_values)

# Calculate P(2.5)
t_interpolate = 2.5
z_interpolated = newton_interpolation(t_values, z_values, t_interpolate)

# Print the result
print(f"A) The interpolated value at t = {t_interpolate} is approximately {z_interpolated:.4f}")

def lagrange_interpolation(t_values, z_values, target_t):
    result = 0
    for i in range(len(z_values)):
        term = z_values[i]
        for j in range(len(t_values)):
            if j != i:
                term *= (target_t - t_values[j]) / (t_values[i] - t_values[j])
        result += term
    return result

# Given data
t_values = [2, 2.1, 2.2, 2.7, 3, 3.4]
z_values = [6, 7.752, 10.256, 36.576, 66, 125.168]

# Target value
target_t = 2.5

# Calculate Lagrange interpolating polynomial at t = 2.5
interpolated_z = lagrange_interpolation(t_values, z_values, target_t)

print(f"B) Interpolated z at t = {target_t}: {interpolated_z}")