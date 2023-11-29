#Question 3

import numpy as np

# Coefficients matrix
A = np.array([[2, 1, -1],
              [5, 2, 2],
              [3, 1, 1]], dtype=float)

# Constants vector
B = np.array([2, 9, 5], dtype=float)

# Augmented matrix [A|B]
augmented_matrix = np.column_stack((A, B))

# Number of equations
n = len(B)

# Print the initial augmented matrix
print("Initial Augmented Matrix:")
print(augmented_matrix)
print()

# Perform Gauss-Jordan elimination without pivoting
for i in range(n):
    # Divide the current row by the pivot element to make the diagonal element 1
    pivot = augmented_matrix[i, i]
    augmented_matrix[i, :] /= pivot
    
    # Eliminate elements above and below the pivot
    for j in range(n):
        if j != i:
            factor = augmented_matrix[j, i]
            augmented_matrix[j, :] -= factor * augmented_matrix[i, :]
    
    # Print the current state of the augmented matrix
    print(f"Step {i + 1}:")
    print(augmented_matrix)
    print()

# Extract the solutions
solutions = augmented_matrix[:, -1]

# Print the solutions
print("Solutions:")
for i in range(n):
    print(f"x_{i + 1} = {solutions[i]:.4f}")
