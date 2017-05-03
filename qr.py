import numpy as np 
from math import sqrt

def norm(a):
	return sqrt(np.dot(a,a))

def householder(x):
	v = np.zeros_like(x)
	v[0] = np.sign(x[0])*norm(x)
	v = v+x	 
	print "v"
	print v
	P = np.outer(v,v)
	print "outer pdt"
	print P 
	I = np.identity(np.shape(P)[0])
	print "identity"
	print I 
	print np.dot(v,v)
	P = I - (2./np.dot(v,v))*P 
	return P 

def padding(P,A):
	diff = np.shape(A)[0] - np.shape(P)[1]
	newP = np.zeros((np.shape(P)[0]+diff,np.shape(P)[1]+diff))
	# newP[0,0] = 1
	# newP[1:,1:] = P
	flag = 0
	for i in range(np.shape(newP)[0]):
		for j in range(np.shape(newP)[1]):
			if i==diff:
				flag = 1
				break;
			elif i==j:
				newP[i,j] = 1
			else:
				newP[i,j] = 0
		if flag==1:
			break
	newP[i:,i:] = P
	return newP

def factorization(A):
	nrow = np.shape(A)[0]
	ncol = np.shape(A)[1]
	for i in range(ncol):
		x = A[i:,i]
		print x
		if np.shape(x)[0] == 1:
			break 

		P = householder(x)
		print "P "
		print P 
		if(i==0):
			Q = np.transpose(P)
		else:
			if(np.shape(P)[1] == np.shape(A)[0]):
				Q = np.dot(np.transpose(P),Q)
			else:
				Pdash = padding(P,A)
				Q = np.dot(np.transpose(Pdash),Q)	

		if(np.shape(P)[1] == np.shape(A)[0]):	
			A = np.dot(P,A)			
		else:
			P = padding(P,A)
			A = np.dot(P,A)
		print "A"
		print A 	
	return [np.transpose(Q),A]
	
A = np.array([[12., -51., 4.], [6., 167.,-68.], [-4., 24., -41.]])
[Q,R] = factorization(A)
print "Q"
print Q 
print "R"
print R 		