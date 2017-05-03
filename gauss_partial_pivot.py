#Perform Gauss Elimination with Partial Pivoting

import numpy as np

print "Enter size of matrix"
n = int(raw_input())
print "Enter A"
A = np.array(input())
print "Enter b"
b = np.array(input())


for k in xrange(n-1):
    #Choose largest pivot element below (and including) k-1
    maxindex = abs(A[k:,k]).argmax() + k
    if A[maxindex, k] == 0:
        raise ValueError("Matrix is singular.")
    #Swap rows
    if maxindex != k:
        A[[k,maxindex]] = A[[maxindex, k]]
        b[[k,maxindex]] = b[[maxindex, k]]
    for row in xrange(k+1, n):
        multiplier = A[row][k]/A[k][k]
        #the only one in this column since the rest are zero
        A[row][k] = multiplier
        for col in xrange(k + 1, n):
            A[row][col] = A[row][col] - multiplier*A[k][col]
        #Equation solution column
        b[row] = b[row] - multiplier*b[k]
#print A
#print b
x = np.zeros(n)
k = n-1
x[k] = b[k]/A[k,k]
while k >= 0:
    x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
    k = k-1

print x