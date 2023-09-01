import numpy as np


def halvering_solve(f, a, b, tol):
    # Din kode her :) --->
    m = (a + b) / 2

    if abs(f(m)) < tol:
        return m
    elif f(a) * f(m) < 0:
        return halvering_solve(f, a, m, tol)
    else:
        return halvering_solve(f, m, b, tol)


f = lambda x: x ** 3 - 9  # Hvilken funksjon f er det du skal finne roten av?
# Hva blir maks feil om x_sol skal være riktig med minst 6 desimaler?
maks_feil = 1 * 10 ** (-6)
a = 1  # Hva må startintervallet være?
b = 3  # Hva må startintervallet være?
x_sol = halvering_solve(f, a, b, maks_feil)  # Hva må startintervallet være?
print(x_sol)
