import numpy as np

# Coefficients matrix A and constants vector B
A = np.array([[1, 1, -1],
              [6, 2, 2],
              [-3, 4, 1]], dtype=float)
B = np.array([-3, 2, 1], dtype=float)

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
    # Divide the current row by the pivot element to make the diagonal 1
    pivot = augmented_matrix[i, i]
    augmented_matrix[i, :] /= pivot
    
    # Eliminate elements below the pivot
    for j in range(i + 1, n):
        factor = augmented_matrix[j, i]
        augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

# Back-substitution to find the solutions
solutions = np.zeros(n)
for i in range(n - 1, -1, -1):
    solutions[i] = augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i + 1:n], solutions[i + 1:n])

# Print the solutions
print("Solutions:")
for i in range(n):
    print(f"x_{i + 1} = {solutions[i]:.4f}")
