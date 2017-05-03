import numpy as np 
from math import sqrt

def norm(a):
	return sqrt(np.dot(a,a))

def gschmidt(A):
	B = np.zeros_like(A)
	for i in range(A.shape[0]):
		if i==0:
			B[0] = A[0]
		else:
			y = np.zeros_like(A[i])
			for j in range(i):
				y = y + (np.dot(A[i],B[j]))/(norm(B[j])**2)*B[j]
			B[i] = A[i] - y
		print i,B[i]

	for i in range(B.shape[0]):
		B[i] = B[i]/norm(B[i])
	return B	
		
mat = np.array([[1.,-1.,0.,0.],[2.,0.,1.,0.],[6.,2.,7.,0.]])
ans = gschmidt(mat)
print ans