#Question 2

import numpy as np

# Coefficients matrix
A = np.array([[8, 2, -2],
              [10, 2, 4],
              [12, 2, 2]], dtype=float)

# Constants vector
B = np.array([8, 16, 16], dtype=float)

# Augmented matrix [A|B]
augmented_matrix = np.column_stack((A, B))

# Number of equations
n = len(B)

# Print the initial augmented matrix
print("Initial Augmented Matrix:")
print(augmented_matrix)
print()

# Perform Gaussian elimination with partial pivoting
for i in range(n):
    # Find the pivot element (the largest element in the current column)
    max_row = np.argmax(abs(augmented_matrix[i:, i])) + i
    augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]
    
    # Divide the current row by the pivot element to make the diagonal element 1
    pivot = augmented_matrix[i, i]
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
