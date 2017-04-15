from math import *
import numpy as np
import numpy.polynomial.legendre as npl
import matplotlib.pyplot as plt 
import newton as nr

#arguments of the Newton-Raphson methods
epsilon = 0.0005
iteration_number = 1000

#return the jacobian matrix of nablaE with the same vector.
def jacobian_electrostatic(E):
    n = len(E)
    J = np.empty((n,n))
    for i in range (0, n):
        #triangle inferior
        for j in range(0, i):
           J[i][j] = 1/(pow((E[i] - E[j]),2))

        #diagonal
        J[i][i] = -(1.0/pow(E[i]-1.0,2)) - (1.0/pow(E[i]+1.0,2))
        for k in range (0, i):
            J[i][i] -= 1/(pow((E[i] - E[k]),2))
        for k in range (i + 1, n):
            J[i][i] -= 1/(pow((E[i] - E[k]),2))

        #triangle superior
        for j in range(i + 1, n):
            J[i][j] = -1/(pow((E[i] - E[j]),2))

    return J

#return nablaE of the E vector
def energy_electrostatic(E):
    n = len(E)
    F = np.empty(n)
    for i in range (0, n):
        F[i] = (1/(E[i] - 1.0)) + (1/(E[i] + 1.0))
        for j in range (0, i):
            F[i] += 1/(E[i] - E[j])
        for j in range (i + 1, n):
            F[i] += 1/(E[i] - E[j])
    return F

#draw the equilibrium points and the legendre's polynomials.
def draw_electrostatic(E):
    #points of the polynomials.
    xaxis = np.arange(-1,1,0.01)
    
    #vector which F(X) = 0
    X = nr.Newton_Raphson(energy_electrostatic, jacobian_electrostatic, E, iteration_number, epsilon)

    #elements of the vector X
    charges = plt.scatter(X, np.full(len(X), 0))
    colors = "red", "blue", "green", "cyan", "purple", "orange", "magenta" 

    #drawing the 8 first polynomials.
    for n in range (3, 8, 1):
        #array of 0.
        T = np.zeros(n)
        #put the coefficient relate to the polynomial wanted to 1
        T[n - 1] = 1
        #give the polynomial
        L = npl.Legendre(T)
        #the derivative of the polynomial
        D = npl.Legendre.deriv(L)
        yaxis = D(xaxis)
        plt.plot(xaxis, yaxis, color=colors[n-1])

    plt.show()

#size of the vector E
n = 11

#random number between [-1,1]
E = np.random.rand(n) * 2 - 1
#draw the graph
draw_electrostatic(E)
