""" Projectile Motion

Here a projectile is launched many times at angles randomly chosen from a 
specified range at a consistent launch speed. The distribution of resultant
distances will be investigated to determine how likely a projectile is to land 
within tolerance of a certain target distance.
"""
from numpy import zeros, cos, sin, pi, sqrt, linspace
from pylab import figure, title, xlabel, ylabel, show, scatter, subplot, hist, tight_layout
from random import random

# Constants
g = 9.81		# acceleration due to gravity [m/s^2]
dt = 0.01		# time step [s]
rho = 1.225		# desnity of air at sea level 15 Celsius [kg/m^3]
A = 0.0015		# cross-sectional area of our projectile [m^2]
m = 0.05		# mass of our projectile [kg]
Somega = 0.01	# rough backspin constant (Magnus Effect) [kg/s]
theta_min = 1	# minimum launch angle [degrees]
theta_max = 70	# max launch angle [degrees]
TOL = 0.10		# tolerance is 10%
target = 100	# target distance [m]
tol = TOL*target	# tolerance range [m]
N = 5000		# number of trials

# Options
# 1: vacuum
# 2: drag and spin
option = 2


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
	system = 'vacuum'
elif option == 2:
	f = f_drag_spin
	system = 'drag and spin'

# Initialize Arrays for Plotting
distance = zeros(N)		# horizontal distance travelled for each launch angle
launch_angle = zeros(N)
for trial in range(N):
	# Initial Conditions
	theta = theta_min + random()*(theta_max-theta_min)
	v = 70						# launch speed [m/s]
	r = zeros(4)
	r[0], r[1] = 0., 0.			# projectile starts at (0, 0)
	r[2] = v*cos(theta*pi/180)	# x-velocity [m/s]
	r[3] = v*sin(theta*pi/180)	# y-velocity [m/s]
	
	while r[1] >= 0.:			# projectile in air
		r += f(r)*dt
	distance[trial] = r[0]
	launch_angle[trial] = theta

figure(1)
subplot(311)
scatter(launch_angle, distance)
title('Horizontal Distance vs Launch Angle: {}'.format(system))
xlabel('x [m]')
ylabel('y [m]')
subplot(312)
hist(launch_angle, bins=50)
xlabel('launch angle [degrees]')
subplot(313)
hist(distance, bins=50)
xlabel('distance [m]')
tight_layout()
show()

within_tol = ((target - tol < distance) & (distance < target + tol)).sum()
print(100*within_tol/N, 'percent of trials are within tolerance of the target distance:', system)

