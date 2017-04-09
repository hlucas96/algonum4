import numpy as np
import pylab as pl

def Newton_Raphson(f, J, U0, N, epsilon):
    i = 0
    while(i < N and np.linalg.norm(U0) > epsilon):
        U0 = U0 + np.linalg.lstsq(J(U0), -f(U0))[0]

        i += 1
    if (i == N):
        print("Error : Solution not found")
    return U0


def Newton_Raphson_backtracking(f, J, U0, N, epsilon):
    i = 0
    while(i < N and np.linalg.norm(U0) > epsilon):
        last_U = U0
        last = np.linalg.norm(last_U)
        U0 = U0 + np.linalg.lstsq(J(U0), -f(U0))[0]
        while(np.linalg.norm(f(U0)) > last):
            U0 = (last_U + U0)/2
        i += 1
    if (i == N):
        print("Error : Solution not found")
    return U0

def Newton_real(f, f1, x0, N, epsilon):
    i = 0
    x = []
    y = []
    x += [x0]
    y += [0]
    x += [x0]
    y += [f(x0)]
    while(i < N and f(x0) > epsilon):
        x0 = x0 - f(x0)/f1(x0)
        x += [x0]
        y += [0]
        x += [x0]
        y += [f(x0)]
        i += 1
    xf = np.linspace(-20,20,100)
    yf = [f(i) for i in xf]
    pl.grid(True)
    pl.plot(x, y)
    pl.plot(xf, yf)
    pl.show()
