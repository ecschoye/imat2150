def func(x):
    return x**3 - 9


def find_interval_with_length_1():
    x = 0
    while True:
        if func(x) * func(x + 1) <= 0:
            return x, x + 1
        x += 1


a, b = find_interval_with_length_1()

print(f"Interval with length 1: [{a}, {b}]")