''' Simpsons Rule to Integrate Bessel Functions '''
from numpy import cos, sin, pi, linspace
from pylab import figure, plot, title, legend, show
from scipy.special import jv


def integrand(phi, n, x):
	return cos(n*phi - x*sin(phi))/pi


def simpsons(a, b, N, n, x):
	h = (b-a)/N
	s = integrand(a, n, x) + integrand(b, n, x)
	
	for i in range(1, N, 2):
		s += 4*integrand(a + i*h, n, x)
	for j in range(2, N - 1, 2):
		s += 2*integrand(a + j*h, n, x)
		
	return h*s/3

def bessel(n, x):
	return simpsons(0., pi, 1000, n, x)

x = linspace(0, 20, 101)
J0 = bessel(0, x)
J3 = bessel(3, x)
J5 = bessel(5, x)

figure(1)
plot(x, J0, label='J0')
plot(x, J3, label='J3')
plot(x, J5, label='J5')
title('Bessel Functions')
legend()
show()

jvJ0 = jv(0, x)
jvJ3 = jv(3, x)
jvJ5 = jv(5, x)

figure(2)
title('Relative Errors')
plot(x, jvJ0 - J0, label='J0 error')
plot(x, jvJ3 - J3, label='J3 error')
plot(x, jvJ5 - J5, label='J5 error')
legend()
show()
