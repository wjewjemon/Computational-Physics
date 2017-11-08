#SoliveLinear.py
#Python module for PHY407
#Paul Kushner, 2015-09-26
#This module contains useful routines for solving linear systems of equations.
#Based on gausselim.py from Newman
from numpy import empty
#The following will be useful for partial pivoting
from numpy import empty, copy
from numpy import array

#Implement Gaussian Elimination
#This should be non-destructive for input arrays, so we will copy A and v to temporary variables
def GaussElim(A_in,v_in,pivot=False):
    #copy A and v to temporary variables using copy command
    A = copy(A_in)
    v = copy(v_in)
    N = len(v)
    
    for m in range(N):
        
        # partial pivot
        if pivot:
            swap = m
            for i in range(m+1, N):
                if abs(A[i, m]) > abs(A[swap, m]):
                    swap = i
            if swap > m:
                v[swap], v[m] = v[m], v[swap]
                A[m, :], A[swap, :] = copy(A[swap, :]), copy(A[m, :])
    
        # Divide by the diagonal element
        div = A[m,m]
        A[m,:] /= div
        v[m] /= div
    
        # Now subtract from the lower rows
        for i in range(m+1,N):
            mult = A[i,m]
            A[i,:] -= mult*A[m,:]
            v[i] -= mult*v[m]
    
    # Backsubstitution
    #create an array of the same type as the input array
    x = empty(N,dtype=v.dtype)
    for m in range(N-1,-1,-1):
        x[m] = v[m]
        for i in range(m+1,N):
            x[m] -= A[m,i]*x[i] 
    return x
    
def PartialPivot(A_in,v_in):
    return GaussElim(A_in, v_in, pivot=True)


        
