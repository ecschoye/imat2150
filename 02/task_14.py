import numpy as np

def LUfactorize(A):
   n,m = np.shape(A)
   L = np.eye(n)
   U = np.zeros((n,n))
   U = A.copy()
   for j in ????:
      for i in range(?????):
         if ( ???? ): #0 i pivot element
            raise np.linalg.LinAlgError("Zero pivot encountered")
            return 
         mult = ?????
         U[i,j]=0.0
         L[i,j] = ????
         for k in range(???, ???):
            U[?,?] = ?????
   return L,U


# Resten av koden kan du la stå som den er :)   
A = np.array([ 1.0,  2,-1,0,3,1,2,-1,1 ]) #Prøv å skrive "1.0" som "1" - Hva foregår?
A=A.reshape((3,3))
try:
   L,U = LUfactorize(A)
except np.linalg.LinAlgError as e:
   print(f"LinAlgError: {e}")
