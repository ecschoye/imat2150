import sympy as sp

x = sp.symbols('x')

f_expr = 3 / x
g_expr = x ** 2 - 2 * x + 2
h_expr = x ** 2 - 4 * x + 2


def find_fixed_points(func_expr):
    equation = x - func_expr
    solutions = sp.solve(equation, x)
    return solutions


fixed_points_f = find_fixed_points(f_expr)
print(f"Fikspunktene for f(x) = 3 / x er: {fixed_points_f}")

fixed_points_g = find_fixed_points(g_expr)
print(f"Fikspunktene for g(x) = x² - 2x + 2 er: {fixed_points_g}")

fixed_points_h = find_fixed_points(h_expr)
print(f"Fikspunktene for h(x) = x² - 4x + 2 er: {fixed_points_h}")

