''' A 3D plot of a circular membrane that satisfies laplace's eqn for specified
conditions '''
from numpy import cos, sin, pi, sqrt, arange, meshgrid, arctan
from pylab import figure, plot, title, legend, show, cm
from scipy.special import jv
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter



def integrand(phi, n, x):
	return cos(n*phi - x*sin(phi))/pi


def simpsons(a, b, N, n, x):
	h = (b-a)/N
	s = integrand(a, n, x) + integrand(b, n, x)
	
	for i in range(1, N, 2):
		s += 4*integrand(a + i*h, n, x)
	for j in range(2, N - 1, 2):
		s += 2*integrand(a + j*h, n, x)
		
	return h*s/3.


def bessel(n, x):
	return simpsons(0., pi, 1000, n, x)
	

fig = figure(1)
ax = fig.gca(projection='3d')
R0 = 1	# radius of membrane

X = arange(-R0, R0, 0.05*R0)
Y = arange(-R0, R0, 0.05*R0)
X, Y = meshgrid(X, Y)
R = sqrt(X**2 + Y**2)
theta = arctan(Y/X)

# wave eqn on circular membrane U_(3,2) (t=0)
z_32 = 11.620	
U = bessel(2, z_32*R/R0)*cos(2*theta)
U[R>R0] = 0.	# only plot to radius R0
surf = ax.plot_surface(X, Y, U, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

show()
