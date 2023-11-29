#Question 1

import numpy as np

# Coefficients matrix
A = np.array([[10, 2, -1],
              [-3, -6, 2],
              [1, 1, 5]])

# Constants vector
B = np.array([27, -61.5, -21.5])

# Augmented matrix [A|B]
augmented_matrix = np.column_stack((A, B))

# Number of equations
n = len(B)

# Print the initial augmented matrix
print("Initial Augmented Matrix:")
print(augmented_matrix)
print()

# Perform Gaussian elimination
for i in range(n):
    # Pivot element
    pivot = augmented_matrix[i, i]
    
    # Divide the current row by the pivot element to make the diagonal 1
    augmented_matrix[i, :] /= pivot
    
    # Eliminate elements below the pivot
    for j in range(i + 1, n):
        factor = augmented_matrix[j, i]
        augmented_matrix[j, :] -= factor * augmented_matrix[i, :]
    
    # Print the current state of the augmented matrix
    print(f"Step {i + 1}:")
    print(augmented_matrix)
    print()

# Back-substitution to find the solutions
solutions = np.zeros(n)
for i in range(n - 1, -1, -1):
    solutions[i] = augmented_matrix[i, -1]
    for j in range(i + 1, n):
        solutions[i] -= augmented_matrix[i, j] * solutions[j]

# Print the solutions
print("Solutions:")
for i in range(n):
    print(f"x_{i + 1} = {solutions[i]:.4f}")
