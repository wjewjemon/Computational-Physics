''' Applying Numerical Integration

Here I apply the Trapezoidal Rule and Simpson's Rule to perform numerical
integration.
'''
from numpy import pi
from errors import relative_error

def f(x):		# a function to integrate
	return 4/(1+x**2)
	
def trapezoidal(f, a, b, N):
	h = (b-a)/N		# slice width
	s = .5*(f(a) + f(b))
	
	for i in range(1, N):
		s += f(a + i*h)
		
	return h*s
	
def simpsons(f, a, b, N):
	h = (b-a)/N
	s = f(a) + f(b)
	
	for i in range(1, N, 2):
		s += 4*f(a + i*h)
	for j in range(2, N - 1, 2):
		s += 2*f(a + j*h)
		
	return h*s/3
	
N = 1000		# slices
a, b = 0., 1.	# start and end point of integration

t = trapezoidal(f, a, b, N)
s = simpsons(f, a, b, N)
if __name__ == '__main__':
	print(t)
	print(s)
	# use numpy.pi as the actual value of pi
	print('relative errors:')
	print('trapezoidal:', relative_error(pi, t))
	print("simpson's:", relative_error(pi, s))
