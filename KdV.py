import numpy as np
# import scipy.optimize as spyo
from newton import Newton_Raphson


delta_t = 1
delta_x = 0.1
epsilon = 0.1

# global vector and matrix
size = 3
Un = np.empty(size)
DG_matrix = np.empty([size, size])

# constantes pour G
delta_2x = delta_x * 2
a = epsilon / (4 * delta_x)
b = epsilon / (12 * (delta_x ** 3))

# constantes pour DG
i_plus_2  = epsilon / (12 * (delta_x ** 3)) 
i_diag    = epsilon / (4 * delta_x)
i_minus_2 = - i_plus_2
c = (1 / delta_2x) - (2 * i_plus_2)



# init Un and GD_matrix
def init_kdv(X0):
        global Un, DG_matrix
        
        n = len(X0)
        Un = np.copy(X0)
        
        DG_matrix = np.zeros([n, n])
        # diagonal
        for i in range(n):
                DG_matrix[i][i] = i_diag
        # diagonal +2 and -2
        for i in range(n - 2):
                DG_matrix[i][i + 2] = i_plus_2
                DG_matrix[i + 2][i] = i_minus_2
        DG_uptade(X0)

# update DG_matrix,
# juste need to change two diagonal thus O(n)
def DG_uptade(U):
        global GD_matrix
        n = len(U)
        # diagonal +1 and -1
        for i in range(n - 1):
                DG_matrix[i][i + 1] =  c + (i_diag * (U[i] + (2 * U[i + 1])))
                DG_matrix[i + 1][i] = -c - (i_diag * (U[i] + (2 * U[i - 1])))

def DG(U):
        DG_uptade(U)
        return DG_matrix

# return the vector G(U)
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

def F(U):
	return ((U - Un) / delta_t) + G((Un + U) / 2)

def DF(U):
        return ((1/delta_t) * np.identity(len(U)) + (DG((U - Un) / 2) / 2))

def next_kdv(U):
        global Un
        Un = Newton_Raphson(F, DF, U, 8, 0.01)
        return Un


np.set_printoptions(suppress=True)

