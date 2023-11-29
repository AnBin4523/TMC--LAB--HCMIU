#Ngo Le Thien An - ITITDK21030
#Q2_A

# Define the function f(x, y)
def f(x, y):
    return 3.5 * x + 2 * y + x**2 - x**4 + 2 * x * y - y**2

# Initialize initial guesses
x = 0
y = 0

# Set the step size
h = 0.1

# Perform three iterations
for iteration in range(3):
    # Calculate the gradient of f(x, y) with respect to x and y
    df_dx = 3.5 + 2 * x - 4 * x**3 + 2 * y
    df_dy = 2 - 2 * y + 2 * x

    # Update x and y using gradient ascent
    x = x + h * df_dx
    y = y + h * df_dy

    # Calculate the new value of the function
    result = f(x, y)

    # Print the results for each iteration
    print(f'Iteration {iteration + 1}:')
    print(f'x = {x:.4f}, y = {y:.4f}, f(x, y) = {result:.4f}\n')

    print(f'Estimated Maximum: x = {x:.4f}, y = {y:.4f}, f(x, y) = {result:.4f}\n')

