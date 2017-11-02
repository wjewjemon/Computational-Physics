''' Timing Matrix Multiplication

Here we compare the time it takes to multiply matrices using a standard method 
and a built in numpy method.
'''
from time import clock
from numpy import arange, zeros, ones, dot
from pylab import figure, plot, title, xlabel, ylabel, show, legend, subplot, tight_layout

N = arange(2, 101, 5)	# widths of NxN matrices to multiply

# initialize lists to hold calculation times
std = []
np = []

for n in N:
	A = ones([n, n], float)*2.
	B = A
	C = zeros([n, n], float)
	
	start = clock()		# start time of calculation
	for i in range(n):
		for j in range(n):
			for k in range(n):
				C[i, j] += A[i, k]*B[k, j]
	end = clock()		# end time of calculation
	std.append(end-start)
	
	start = clock()
	C = dot(A, B)
	end = clock()
	np.append(end-start)

figure(1)
subplot(211)
title('time vs matrix size for matrix multiplication')
plot(N, std, 'b', label='my method')
plot(N, np, 'r', label='numpy method')
xlabel('N')
ylabel('time [s]')
legend()
subplot(212)
plot(N**3, std, 'b')
xlabel('N^3')
ylabel('time [s]')
tight_layout()
show()
