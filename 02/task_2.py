import numpy

def fikspunkt_solve(f, x0, tol):
    x = x0
    while abs(f(x)) > tol:
        x = f(x)
        error = abs(x - x0)  # Use the updated value of x instead of x0
        print(f"Error: {error}")
        if error < tol:
            break
    return x

f1 = lambda x: x ** 3 - 2 * x - 2
f2 = lambda x: numpy.exp(x) + x - 7  # Provide an argument to numpy.exp()
f3 = lambda x: numpy.exp(x) + numpy.sin(x) - 4

funcs = [f1, f2, f3]
maks_feil = 1 * 10 ** (-8)
sols = []

for f in funcs:
    x_sol = fikspunkt_solve(f, 1, maks_feil)
    sols.append(x_sol)

print(f"Løsning til første ligning x = {sols[0]}")
print(f"Løsning til andre ligning x = {sols[1]}")
print(f"Løsning til tredje ligning x = {sols[2]}")
