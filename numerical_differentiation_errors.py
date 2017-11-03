''' Here I will attempt to show that the optimal step size for forward 
differentiation schemes is sqrt(C) ~= 10^-8.
If step size is too small rounding error will dominate. If step size is too 
large truncation error will dominate.
'''
from math import exp
from numpy import zeros
from pylab import figure, plot, show, xscale, yscale, legend, title, xlabel, ylabel

def f(x):
	return exp(-x**2)
	

def forward(f, x, h):	# forward difference differentiation
	return (f(x+h)-f(x))/h


def central(f, x, h):
	return (f(x+h/2.)-f(x-h/2.))/h

# dfdx at x = 0.5
analytic = -0.778800783

# initialize arrays
h = zeros(17)			# step size
numerical_f = zeros(17)	# numerical derivative, forward
numerical_c = zeros(17)	# numerical derivative, central
rel_err_f = zeros(17)	# relative error, forward diff
rel_err_c = zeros(17)	
for i in range(17):
	h[i] = 10.**-i
	numerical_f[i] = forward(f, .5, h[i])
	numerical_c[i] = central(f, .5, h[i])
	rel_err_f[i] = abs((analytic - numerical_f[i])/analytic)
	rel_err_c[i] = abs((analytic - numerical_c[i])/analytic)


figure(1)
plot(h, rel_err_f, label='forward')
plot(h, rel_err_c, label='central')
xlabel('log(h)')
ylabel('log(relative error)')
legend()
xscale('log')
yscale('log')
show()
