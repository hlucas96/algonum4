import numpy as np

def Newton_Raphson(f, J, U0, N, epsilon):
    i = 0
    while(i < N and np.linalg.norm(U0 - f(U0)) > epsilon):
        U0 = np.linalg.lstsq(J(U0), f(U0))
        i += 1
    return UO

def Newton_real(f, f1, x0, N, epsilon):
    i = 0
    x = []
    y = []
    while(i < N and np.linalg.norm(x0 - f(x0)) > epsilon):
        x0 = np.linalg.lstsq((x0), f(x0))
        i += 1
    return xO
