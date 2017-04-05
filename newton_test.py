import numpy as np
import newton as nw

def f(x):
    return 0.01*(x**3) - 2*x + 2
def f1(x):
    return 0.03*(x**2) - 2

nw.Newton_real(f, f1, 19, 100, 0.01)
