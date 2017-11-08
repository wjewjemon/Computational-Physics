#SoliveLinear.py Modified for 1a
from numpy import empty, copy, array
#Implement Gaussian Elimination and Partial Pivoting
#This should be non-destructive for input arrays, so we will copy A and v to temporary variables
def PartialPivot(A_in,v_in):
    #copy A and v to temporary variables using copy command
    A = copy(A_in)
    v = copy(v_in)
    N = len(v)
    for m in range(N):
        #if not zero use Gaussian Elimintaion
        if A[m,m] > 1.0e-16:
            #print('gauss')
            #Division by the diagonal element
            div = A[m,m]
            A[m,:] /= div
            v[m] /= div

        # Now subtract from the lower rows
            for i in range(m+1,N):
                mult = A[i,m]
                A[i,:] -= mult*A[m,:]
                v[i] -= mult*v[m]
            
        #if zero must pivot the Element using partial pivots
        else:
            #print('partial')
            p = m
            for i in range(m+1,N):
                #finding the pivot point
                if abs(A[i,m]) > abs(A[p,m]):
                    p = i
                    
            #Replacing the rows
            A[p,:], A[m,:] = copy(A[m,:]), copy(A[p,:])
            v[p] , v[m] = copy(v[m]), copy(v[p])
           

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
    

    
