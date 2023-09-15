import numpy as np


def euler(f, y_init, start, stop, h):
    n = int((stop - start) / h) + 1  # Number of steps
    t = np.linspace(start, stop, n)  # Time grid
    y = np.zeros((n, len(y_init)))  # Initialize y array with zeros
    y[0, :] = y_init  # Initial condition

    for i in range(1, n):
        y[i, :] = y[i - 1, :] + h * f(y[i - 1, :])

    return t, y


def y_exact(t):
    return np.array([3 * np.exp(-t) + 2 * np.exp(4 * t), -2 * np.exp(-t) + 2 * np.exp(4 * t)])


# Define the ODE system function
f = lambda y: np.array([y[0] + 3 * y[1], 2 * y[0] + 2 * y[1]])

# Initial conditions
y_init = np.array([5, 0])

# Run Euler's method
t, y = euler(f, y_init, 0, 1, 0.25)
