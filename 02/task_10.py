import numpy as np

# Define the naive Gaussian elimination function
def naive_gauss(A, b):
    n, m = np.shape(A)

    # Create an augmented matrix S by combining A and b
    S = np.zeros((n, n + 1))
    S[:, 0:n] = A
    S[:, -1] = b

    # Perform Gaussian elimination
    for j in range(n - 1): # Loop over columns
        for i in range(j + 1, n): # Loop over rows below the diagonal
            # Calculate the multiplier for row elimination
            mult = S[i, j] / S[j, j]
            S[i, j] = 0.0
            for k in range( j + 1, n + 1 ):  # Loop over columns
                # Update the values in the current row
                S[i,k] = S[i,k] - mult * S[j,k]

            # Solving for the solution vector x
            x = S[:, -1]
            for i in range(n - 1, -1, -1): # Iterate from last row to first row
                for j in range(i + 1, n): # Iterate over remaining columns
                    x[i] = x[i] - ????
                x[i] = x[i] / S[?, ?]  # Calculate the sum of products of coefficients and solution values

    return x

# Forslag til fremgangsmåte til definere A, b
# -Viser noen nyttige np-funksjoner

# Define the coefficient matrix A and the b vector
A = np.array([ [1, 2, -1], [0, 3, 1], [2, -1, 1]])
A = A.reshape((3, 3))
b = np.array([2,4,2]).T

# Apply the naive Gaussian elimination function to solve the system of linear equations
x = naive_gauss(A, b)

print(x)