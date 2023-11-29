# Ngô Lê Thiên Ân - ITITDK21030
import numpy as np

# From question
A = np.array([
    [3, -0.1, -0.2],
    [0.1, 7, -0.3],
    [0.3, -0.2, 10]
])
B = np.array([7.85, -19.3, 71.4])

# Augmented matrix [A|B]
augmented_matrix = np.column_stack((A, B))

# Perform Gaussian elimination
n = len(B)
for i in range(n):
    # Make the diagonal element 1
    diagonal_element = augmented_matrix[i, i]
    augmented_matrix[i, :] /= diagonal_element

    # Eliminate other elements in the current column
    for j in range(i+1, n):
        factor = augmented_matrix[j, i]
        augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

# Back-substitution to get the solutions
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:n], x[i+1:n])

# Print the solutions
print("Solution:")
for i in range(n):
    print(f"x{i+1} = {x[i]:.2f}")
