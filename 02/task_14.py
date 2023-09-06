import numpy as np

def LUfactorize(A):
   n, m = np.shape(A)
   L = np.eye(n)
   U = np.zeros((n, n))
   U[:] = A  # Copy A into U

   for j in range(n):
      for i in range(j+1, n):
         if U[j, j] == 0.0:  # Check if the pivot element is zero
            raise np.linalg.LinAlgError("Zero pivot encountered")
            return
         mult = U[i, j] / U[j, j]
         U[i, j] = 0.0
         L[i, j] = mult
         for k in range(j+1, n):
            U[i, k] -= mult * U[j, k]

   return L, U

# Resten av koden kan du la stå som den er :)
A = np.array([1.0, 2, -1, 0, 3, 1, 2, -1, 1])
A = A.reshape((3, 3))

try:
   L, U = LUfactorize(A)
except np.linalg.LinAlgError as e:
   print(f"LinAlgError: {e}")
