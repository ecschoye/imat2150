import numpy as np


def trapezoidal_method(f, y_init, start, stop, h):
    # Calculate the number of steps
    n = int((stop - start) / h) + 1

    # Create an array for time steps
    t = np.linspace(start, stop, n)

    # Initialize the solution array
    y = np.zeros((n, len(y_init)))
    y[0, :] = y_init

    # Main loop for the trapezoidal method
    for i in range(1, n):
        t_prev, y_prev = t[i - 1], y[i - 1, :]
        k1 = f(t_prev, y_prev)
        k2 = f(t[i], y_prev + h * k1)
        y[i, :] = y_prev + 0.5 * h * (k1 + k2)

    return t, y


def f(t, y):
    # Define your system of ODEs
    return np.array([y[0] + y[1], -y[0] + y[1]])


def exact_solution(t):
    # Define the exact (analytical) solution
    return np.array([np.exp(t) * np.cos(t), -np.exp(t) * np.sin(t)])


# Initial conditions
y_init = np.array([1, 0])

# Apply the trapezoidal method
t, y = trapezoidal_method(f, y_init, 0, 1, 0.25)

# Calculate the exact solution for comparison
exact = exact_solution(t).T

# Compute the error
error = np.abs(y - exact)

# Display the results
print("t      y[0]          y[1]    error[0]      error[1]")
for i in range(t.size):
    print(f"{t[i]:.2f}   {y[i, 0]:.6f}   {y[i, 1]:.6f}   {error[i, 0]:.6f}   {error[i, 1]:.6f}")
