from pprint import pprint
import numpy as np 

#Ax = b
#N : Number of iterations. 
def jacobi(A,b,N=25,x=None):
    # Initial guess if not provided.                                                                                                                                                             
    if x is None:
        x = np.zeros(len(A[0]))

    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = np.diag(A)
    R = A - np.diagflat(D)

    # Iterate for N times                                                                                                                                                                          
    for i in range(N):
        x = (b - np.dot(R,x)) / D
    return x

A = np.array([[2.0,1.0],[5.0,7.0]])
b = np.array([11.0,13.0])
guess = np.array([1.0,1.0])

sol = jacobi(A,b,N=25,x=guess)

print "A:"
pprint(A)

print "b:"
pprint(b)

print "x:"
pprint(sol)