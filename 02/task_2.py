import numpy as np

def fikspunkt_solve(f, x0, tol, max_iter=100):
    iter_count = 0
    while True:
        x1 = f(x0)
        if abs(x1 - x0) < tol or iter_count >= max_iter:
            return x1
        x0 = x1
        iter_count += 1

f1 = lambda x: (2*x + 2)**(1/3)
f2 = lambda x: np.log(7 - x)
f3 = lambda x: np.log(4 - np.sin(x))

funcs = [f1, f2, f3]
tolerance = 1e-8
sols = []

for f in funcs:
    x_sol = fikspunkt_solve(f, x0=0, tol=tolerance)
    sols.append(x_sol)

print(f"Løsning til første ligning x = {sols[0]:.8f}")
print(f"Løsning til andre ligning x = {sols[1]:.8f}")
print(f"Løsning til tredje ligning x = {sols[2]:.8f}")
