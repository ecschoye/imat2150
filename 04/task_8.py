import numpy as np

def euler(f, y_init, h, t_slutt):
    t = np.arange(0, t_slutt + h, h)
    y = np.zeros((len(t), len(y_init)))
    y[0] = y_init
    for i in range(1, len(t)):
        y[i] = y[i - 1] + h * np.array(f(t[i - 1], y[i - 1]))
    return t, y

def f(t, y):
    y1, y2 = y
    return [y2 + y1, y2 - y1]

y_init = [1, 0]  # initial conditions for y1 and y2
h = 0.25  # step size
t_slutt = 1.0  # end time

t, y = euler(f, y_init, h, t_slutt)

# Display the results
headers = ["t", "y1 (Euler)", "y2 (Euler)"]
print(f"{headers[0]:<10}{headers[1]:<12}{headers[2]:<12}")
for i in range(len(t)):
    print(f"{t[i]:<10.2f}{y[i, 0]:<12.2f}{y[i, 1]:<12.2f}")

# Exact solutions at t = 1
y1_exact = np.exp(1) * np.cos(1)
y2_exact = -np.exp(1) * np.sin(1)

# Euler's method results at t = 1 (last element from your array)
y1_euler = y[-1, 0]
y2_euler = y[-1, 1]

# Calculate the global errors
global_error_y1 = np.abs(y1_exact - y1_euler)
global_error_y2 = np.abs(y2_exact - y2_euler)

print(f"Global error for y1: {global_error_y1}")
print(f"Global error for y2: {global_error_y2}")
