from math import *
import numpy as np
import numpy.polynomial.legendre as npl
import matplotlib.pyplot as plt 
import newton as nr

epsilon = 0.05
iteration_number = 100

def jacobian_electrostatic(E):
    n = len(E)
    J = np.empty((n,n))
    for i in range (0, n):
        for j in range(0, i):
           J[i][j] = -1/(pow((E[i] - E[j]),2))

        J[i][i] = -1/(pow((E[i] + 1),2)) - 1/(pow((E[i] - 1),2))
        for k in range (0, i):
            J[i][i] -= 1/(pow((E[i] - E[k]),2))
        for k in range (i + 1, n):
            J[i][i] -= 1/(pow((E[i] - E[k]),2))

        for j in range(i + 1, n):
            J[i][j] =  -1/(pow((E[i] - E[j]),2))

    return J

def energy_electrostatic(E):
    n = len(E)
    F = np.empty(n)
    for i in range (0, n):
        F[i] = (1/(E[i] + 1)) + (1/(E[i] - 1))
        for j in range (0, i):
            F[i] += 1/(E[i] - E[j])
        for j in range (i + 1, n):
            F[i] += 1/(E[i] - E[j])
        print(F[i])
    return F


def draw_electrostatic(E):
    X = nr.Newton_Raphson(energy_electrostatic, jacobian_electrostatic, E, iteration_number, epsilon)
    charges = plt.scatter(X, np.full(len(X), 2))
    #L = npl.legroots(npl.legder(E))
    #legendre = plt.scatter(L, np.full(len(L), 2), color="r")

    #    plt.legend(charges, "charges positions")
    plt.show()

n = 9
E = np.random.rand(n) * 2 - 1
energy_electrostatic(E)
jacobian_electrostatic(E)
#draw_electrostatic(E)
