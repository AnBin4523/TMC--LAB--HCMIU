import numpy as np
import matplotlib.pyplot as plt

# Given data
t0, x0, y0 = 0, 0, 1
h = 0.25
t_values = np.arange(t0, 1.25, h)

# Function representing the differential equation dy/dx = (1 + 2t) * sqrt(x)
def f(t, x, y):
    return (1 + 2*t) * np.sqrt(x)

# Analytical solution
def analytical_solution(t, x):
    return (2/3) * (1 + 2*t) * x**1.5 + 1

# Euler's method
def euler_method(t_values, h):
    x_values_euler = [x0]
    y_values_euler = [y0]

    for t in t_values[:-1]:
        x_next = x_values_euler[-1] + h
        y_next = y_values_euler[-1] + h * f(t, x_values_euler[-1], y_values_euler[-1])
        x_values_euler.append(x_next)
        y_values_euler.append(y_next)

    return x_values_euler, y_values_euler

# Heun's method without iteration
def heun_method(t_values, h):
    x_values_heun = [x0]
    y_values_heun = [y0]

    for t in t_values[:-1]:
        k1 = h * f(t, x_values_heun[-1], y_values_heun[-1])
        k2 = h * f(t + h, x_values_heun[-1] + h, y_values_heun[-1] + k1)
        x_next = x_values_heun[-1] + h
        y_next = y_values_heun[-1] + 0.5 * (k1 + k2)
        x_values_heun.append(x_next)
        y_values_heun.append(y_next)

    return x_values_heun, y_values_heun

# Ralston's method
def ralston_method(t_values, h):
    x_values_ralston = [x0]
    y_values_ralston = [y0]

    for t in t_values[:-1]:
        k1 = h * f(t, x_values_ralston[-1], y_values_ralston[-1])
        k2 = h * f(t + 2/3 * h, x_values_ralston[-1] + 2/3 * h, y_values_ralston[-1] + 2/3 * k1)
        x_next = x_values_ralston[-1] + h
        y_next = y_values_ralston[-1] + 1/4 * (k1 + 3 * k2)
        x_values_ralston.append(x_next)
        y_values_ralston.append(y_next)

    return x_values_ralston, y_values_ralston

# Fourth-order Runge-Kutta (RK4) method
def rk4_method(t_values, h):
    x_values_rk4 = [x0]
    y_values_rk4 = [y0]

    for t in t_values[:-1]:
        k1 = h * f(t, x_values_rk4[-1], y_values_rk4[-1])
        k2 = h * f(t + h/2, x_values_rk4[-1] + h/2, y_values_rk4[-1] + k1/2)
        k3 = h * f(t + h/2, x_values_rk4[-1] + h/2, y_values_rk4[-1] + k2/2)
        k4 = h * f(t + h, x_values_rk4[-1] + h, y_values_rk4[-1] + k3)
        x_next = x_values_rk4[-1] + h
        y_next = y_values_rk4[-1] + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        x_values_rk4.append(x_next)
        y_values_rk4.append(y_next)

    return x_values_rk4, y_values_rk4

# Analytical solution
y_analytical = analytical_solution(t_values, x0)

# Euler's method
x_euler, y_euler = euler_method(t_values, h)

# Heun's method without iteration
x_heun, y_heun = heun_method(t_values, h)

# Ralston's method
x_ralston, y_ralston = ralston_method(t_values, h)

# Fourth-order Runge-Kutta (RK4) method
x_rk4, y_rk4 = rk4_method(t_values, h)

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(t_values, y_analytical, label='Analytical Solution', marker='o', linestyle='-', color='black')
plt.plot(x_euler, y_euler, label="Euler's Method", marker='o', linestyle='-', color='blue')
plt.plot(x_heun, y_heun, label="Heun's Method", marker='o', linestyle='-', color='green')
plt.plot(x_ralston, y_ralston, label="Ralston's Method", marker='o', linestyle='-', color='orange')
plt.plot(x_rk4, y_rk4, label="RK4 Method", marker='o', linestyle='-', color='red')

plt.title("Numerical Solutions of dy/dx = (1 + 2t) sqrt(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
