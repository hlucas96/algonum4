import numpy as np
import newton as nw

def g(x):
    return 0.01*(x**3) - 2*x + 2
def g1(x):
    return 0.03*(x**2) - 2

nw.Newton_real(g, g1, 24, 100, 0.01, -20, 25)

def f(x):
    return -0.0044*(x**4) -0.0023*(x**3) + 0.4089*(x**2) +0.3579*x -3
def f1(x):
    return -0.0176*(x**3) -0.0069*(x**2) + 0.8178*x + 0.3579

x0 = -6.65
N = 10
a = -11
b = 12
nw.Newton_real(f, f1, x0, N, 0.01, a, 16.11)
nw.Newton_real_backtracking(f, f1, x0, N, 0.01, a, b)
