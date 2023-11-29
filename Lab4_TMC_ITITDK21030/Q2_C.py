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

# Perform Gauss-Jordan elimination without partial pivoting
for i in range(n):
    # Divide the current row by the pivot element to make the diagonal 1
    pivot = augmented_matrix[i, i]
    augmented_matrix[i, :] /= pivot
    
    # Eliminate elements above and below the pivot
    for j in range(n):
        if j != i:
            factor = augmented_matrix[j, i]
            augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

# Extract the solutions from the last column of the augmented matrix
solutions = augmented_matrix[:, -1]

# Print the solutions
print("Solutions:")
for i, solution in enumerate(solutions):
    print(f"x_{i + 1} = {solution:.4f}")
