import numpy as np

size = 10

delta_t = 0.1
delta_x = 0.1
epsilon = 0.1

delta_2x = delta_x * 2
a = epsilon / (4 * delta_x)
b = epsilon / (12 * (delta_x ** 3))

U_n = np.empty(size)

def G(U):
	n = len(U)
	V = np.empty(n)
	for i in range (0, n - 2):
		V[i] = (U[i+1] - U[i-1]) / delta_2x
		V[i] += a * (U[i+1] - U[i-1]) * (U[i-1] + U[i] + U[i+1])
		V[i] += b * (U[i+2] - 2*U[i+1] + 2*U[i-1] - U[i-2])

	i = n - 2 
	V[i] = (U[i+1] - U[i-1]) / delta_2x
	V[i] += a * (U[i+1] - U[i-1]) * (U[i-1] + U[i] + U[i+1])
	V[i] += b * (U[0] - 2*U[i+1] + 2*U[i-1] - U[i-2])

	i = n - 1
	V[i] = (U[0] - U[i-1]) / delta_2x
	V[i] += a * (U[0] - U[i-1]) * (U[i-1] + U[i] + U[0])
	V[i] += b * (U[1] - 2*U[0] + 2*U[i-1] - U[i-2])

	return V


def F(X):
	return ((X - U_n) / delta_t) + G((U_n + X) / 2)
	
	
