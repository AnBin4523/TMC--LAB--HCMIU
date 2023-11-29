#Question 4

import numpy as np

# Coefficients matrix
A = np.array([[15, -3, -1],
              [-3, 18, -6],
              [-4, -1, 12]], dtype=float)

# Constants vector
B = np.array([3300, 1200, 2400], dtype=float)

# Number of equations
n = len(B)

# Initialize the solution vector
solution = np.zeros(n, dtype=float)

# Tolerance (ε_s)
epsilon_s = 0.05  # 5%

# Perform Gauss-Seidel iterations
max_iterations = 100  # Set a maximum number of iterations to prevent infinite loops
for iteration in range(max_iterations):
    previous_solution = solution.copy()
    for i in range(n):
        summation = 0
        for j in range(n):
            if i != j:
                summation += A[i, j] * solution[j]
        solution[i] = (B[i] - summation) / A[i, i]

    # Calculate the approximate relative error
    approximate_relative_error = np.max(np.abs(solution - previous_solution) / np.abs(solution + np.finfo(float).eps))

    print(f"Iteration {iteration + 1}: {solution}, Approx. Relative Error = {approximate_relative_error:.6f}")

    # Check for convergence
    if approximate_relative_error < epsilon_s:
        print("Converged.")
        break
else:
    print("Did not converge within the maximum number of iterations.")
