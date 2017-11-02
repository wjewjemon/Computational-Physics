''' errors

Two-pass and one-pass standard deviation calculation methods are compared. Their 
relative errors are calculated using numpy.std as the correct value.
'''
from numpy import loadtxt, sqrt, std


def two_pass(data):
	n = len(data)

	mean = 0.
	for value in data:
		mean += value
	mean /= n

	var = 0
	for value in data:
		var += (value - mean)**2
	var /= n - 1
	
	sigma = sqrt(var)
	return sigma
	
	
def one_pass(data):
	n = len(data)
	
	mean = 0
	tmp = 0
	for value in data:
		mean += value
		tmp += value**2
	mean /= n
	if n*mean**2 > tmp:
		print("Can't take the square root of a negative number.")
		return -1
	tmp -= n*mean**2
	
	sigma = sqrt(tmp/(n-1))
	return sigma
	
	
def relative_error(actual, approximate):
	return abs((actual-approximate)/actual)
	
data = loadtxt('cdata.txt')
actual = std(data, ddof=1)
approx1 = one_pass(data)
approx2 = two_pass(data)

print("1:", relative_error(actual, approx1))
print("2:", relative_error(actual, approx2))
