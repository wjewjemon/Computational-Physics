""" Projectile Motion

Here I simulate the motion of a small projectile. At first, only gravity is accounted for as I tackle projectile motion in a vacuum. Later on the effects of drag and spin are considered to account for air resistance.
Euler's method is used for numerical integration to simulate the trajectory of the projectile.
"""
from numpy import zeros, arange, cos, sin, pi, sqrt, argmax
from pylab import figure, plot, title, xlabel, ylabel, show

# Constants
g = 9.81		# acceleration due to gravity [m/s^2]
dt = 0.01		# time step [s]
rho = 1.225		# desnity of air at sea level 15 Celsius [kg/m^3]
A = 0.0015		# cross-sectional area of our projectile [m^2]
m = 0.05		# mass of our projectile [kg]
Somega = 0.01	# rough backspin constant (Magnus Effect) [kg/s]

# Options
# 1: vacuum
# 2: drag, no spin
# 3: drag and spin
option = 3


def C(v):		# drag coefficient
	if v < 14:
		return 0.5
	return 7./v

# ODEs to be solved
def f_vacuum(r):
	dfdt = zeros(4)	
	
	dfdt[0] = r[2]	# dx/dt
	dfdt[1] = r[3]	# dy/dt
	dfdt[2] = 0.	# dv_x/dt
	dfdt[3] = -g	# dv_y/dt
	
	return dfdt


def f_drag(r):
	dfdt = zeros(4)	
	
	v = sqrt(r[2]**2 + r[3]**2)	# projectile speed [m/s]
	dfdt[0] = r[2]	
	dfdt[1] = r[3]	
	dfdt[2] = -C(v)*rho*A*r[2]*v/m		
	dfdt[3] = -g - C(v)*rho*A*r[3]*v/m	
	
	return dfdt


def f_drag_spin(r):
	dfdt = zeros(4)	
	
	v = sqrt(r[2]**2 + r[3]**2)
	dfdt[0] = r[2]
	dfdt[1] = r[3]	
	dfdt[2] = -(C(v)*rho*A*r[2]*v + Somega*r[3])/m		
	dfdt[3] = -g - (C(v)*rho*A*r[3]*v - Somega*r[2])/m	
	
	return dfdt
	

if option == 1:
	f = f_vacuum
	launch_angles = arange(5, 86, 5)	
	system = 'vacuum'
elif option == 2:
	f = f_drag
	launch_angles = arange(5, 86, 5)	
	system = 'drag'
elif option == 3:
	f = f_drag_spin
	launch_angles = arange(.5, 20.1, .5)	
	system = 'drag and spin'


distance = []		# horizontal distance travelled for each launch angle
for theta in launch_angles:
	# Initial Conditions
	v = 70						# launch speed [m/s]
	r = zeros(4)
	r[0], r[1] = 0., 0.			# projectile starts at (0, 0)
	r[2] = v*cos(theta*pi/180)	# x-velocity [m/s]
	r[3] = v*sin(theta*pi/180)	# y-velocity [m/s]
	
	while r[1] >= 0.:			# projectile in air
		r += f(r)*dt
	distance.append(r[0])


figure(1)
plot(launch_angles, distance)
title('Horizontal Distance vs Launch Angle: {}'.format(system))
show()
	
# Initialize Lists for Plotting Trajectory
max_index = argmax(distance)
max_theta = launch_angles[max_index]
v = 70						# launch speed [m/s]
r = zeros(4)
r[0], r[1] = 0., 0.			# projectile starts at (0, 0)
r[2] = v*cos(max_theta*pi/180)	# x-velocity [m/s]
r[3] = v*sin(max_theta*pi/180)	# y-velocity [m/s]
x_optimal = []
y_optimal = []

while r[1] >= 0.:
	x_optimal.append(r[0])
	y_optimal.append(r[1])
	
	r += f(r)*dt
	
figure(2)
plot(x_optimal, y_optimal)
title('Optimal Launch Angle ({} degrees) Trajectory: {}'.format(max_theta, system))
xlabel('x [m]')
ylabel('y [m]')
show()

