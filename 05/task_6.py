import numpy as np
from numpy.linalg import solve


def getNAK_System(x_coords, y_coords):
    n = x_coords.size  # Antall punkter

    # delta_i = x_(i+1) - x_i
    delta = np.array([x_coords[i] - x_coords[i - 1] for i in range(1, n)])

    # BigDelta_i = y_(i+1) - y_i
    BigDelta = np.array([y_coords[i] - y_coords[i - 1] for i in range(1, n)])

    A = np.zeros((n, n))
    # Man kan fylle diagonaler i numpy feks slik:
    lowerDiag = np.array([delta[i] for i in range(n - 1)])
    # negativ indeksering indekserer baklengs x[-1] = siste element
    lowerDiag[-1] = 1
    # Før vi fyller diagonalen slicer vi matrisen A slik at
    # diagonalen like under hoveddiagonal blir den nye hoveddiagonalen
    # (vi fyller hovediagonalen på matrisen vi får ved å fjerne øverste rad og siste kolonne)
    np.fill_diagonal(A[1:, :-1], lowerDiag)

    mainDiag = np.ones(n)
    mainDiag[-1] = -1
    mainDiag[1:-1] = np.array([2 * (delta[i] + delta[i - 1]) for i in range(1, n - 1)])

    upperDiag = np.array([delta[i] for i in range(n - 1)])
    upperDiag[0] = -1

    np.fill_diagonal(A, mainDiag)
    np.fill_diagonal(A[:-1, 1:], upperDiag)

    b = np.zeros(n)
    b[1:-1] = np.array([3 * (BigDelta[i] / delta[i] - BigDelta[i - 1] / delta[i - 1]) for i in range(1, n - 1)])

    return A, b


def getNAK_splines(A, b, x_coords, y_coords):
    n = x_coords.size
    delta = np.array([x_coords[i] - x_coords[i - 1] for i in range(1, n)])
    BigDelta = np.array([y_coords[i] - y_coords[i - 1] for i in range(1, n)])

    # Bruk solve til å løse likningssettet
    c = solve(A, b)
    d = [(c[i] - c[i - 1])/(3*delta[i-1]) for i in range(1, n)]
    b = [BigDelta[i - 1] / delta[i - 1] - delta[i - 1] / 3 * (c[i] + 2 * c[i - 1]) for i in range(1, n)]
    a = [y_coords[i] for i in range(0, n)]
    return a, b, c, d


x = np.array([1, 2, 4, 5., 7, 9])
y = np.array([2, 1, 4, 3., 0, 2])
n = x.size
A, bs = getNAK_System(x, y)
a, b, c, d = getNAK_splines(A, bs, x, y)