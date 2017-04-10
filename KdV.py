import numpy as np
from newton import Newton_Raphson
# np.set_printoptions(suppress=True) # for beauty



def init_constante(dx, dt, eps):
        global delta_x, delta_t, epsilon, \
                delta_2x, a, b, \
                i_plus_2, i_diag, i_minus_2, c 

        delta_t = dt
        delta_x = dx
        epsilon = eps
        
        # constantes for G
        delta_2x = dx * 2
        a = eps / (4 * dx)
        b = eps / (12 * (dx ** 3))

        # constantes for DG
        i_plus_2  = eps / (12 * (dx ** 3)) 
        i_diag    = eps / (4 * dx)
        i_minus_2 = - i_plus_2
        c = (1 / delta_2x) - (2 * i_plus_2)


# init Un and GD_matrix
def init_kdv(X0, dx, dt, eps):
        global Un, DG_matrix

        init_constante(dx, dt, eps)
        
        n = len(X0)
        Un = np.copy(X0)
        
        DG_matrix = np.zeros([n, n])
        # diagonal +2 and -2
        for i in range(n - 2):
                DG_matrix[i][i + 2] = i_plus_2
                DG_matrix[i + 2][i] = i_minus_2
        DG_update(X0)

        
# update DG_matrix,
# juste need to change two diagonal thus O(n)
def DG_update(U):
        global GD_matrix
        n = len(U)
        # diagonal +1 and -1
        for i in range(n - 1):
                DG_matrix[i][i + 1] =  c + (i_diag * (U[i] + (2 * U[i + 1])))
                DG_matrix[i + 1][i] = -c - (i_diag * (U[i] + (2 * U[i - 1])))
        # diagonal
        for i in range(n - 1):
                DG_matrix[i][i] = i_diag * (U[i - 1] + U[i + 1])
        i = n - 1
        DG_matrix[i][i] = i_diag * (U[i - 1] + U[0])

        
def DG(U):
        DG_update(U)
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
        Un = Newton_Raphson(F, DF, U, 8, 1)
        return Un


