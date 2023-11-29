import math

# Define the function and its derivative
def f(x):
    return x**4 * math.exp(-3 * x**2)

def f_prime(x):
    return 4 * x**3 * math.exp(-3 * x**2) - 6 * x * x**4 * math.exp(-3 * x**2)

# Define the point of evaluation
x_exact = 0.5
x0 = 1.0

# Calculate the exact value
exact_value = f(x_exact)

# Calculate the first-order Taylor series approximation
approximation = f(x0) + f_prime(x0) * (x_exact - x0)

# Print the results
print("Exact Value:", exact_value)
print("Approximation:", approximation)
print("Comparison:")
print("Exact Value - Approximation:", exact_value - approximation)
