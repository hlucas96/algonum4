from math import *
import numpy as np
import matplotlib as plt 
import newton as nr

epsilon = 0.05
iteration_number = 10

def energy_electrostatic(E):
    x = 0
    for i in range (0, n):
        x += log(abs(E[i] + 1)) + log(abs(E[i] - 1))
        s = 0
        for j in range (0, i):
            s += log(abs(E[i] - E[j]))
        for j in range (i + 1, n):
            s += log(abs(E[i] - E[j]))
        x += (s/2)
    return x

def jacobian_electrostatic(E):
    n = len(E)
    J = np.empty(n)
    for i in range (0, n):
        J[i] = (1/(E[i] + 1)) + (1/(E[i] - 1))
        for j in range (0, i):
            J[i] += 1/(E[i] - E[j])
        for j in range (i + 1, n):
            J[i] += 1/(E[i] - E[j])
    J.shape = (n, 1)
    return J   

def draw_electrostatic(E):
    X = nr.Newton_Raphson(energy_electrostatic, jacobian_electrostatic, E, iteration_number, epsilon)
    charges = plt.plot(E, X, linewidth = 1.0)
    plt.legend([energy], ["charges positions"])
    plt.show()

n = 9
E = np.empty(n)
for i in range (0, n):
    E[i] = (i + 1)/n
E[n - 1] = 8
draw_electrostatic(E)