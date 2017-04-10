import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an

from KdV import init_kdv, next_kdv


fig, ax = plt.subplots()
L = 15.0
N = 200
alpha = 1
dt = 0.8
esp = 0.1

xaxis = np.empty(N)
yaxis = np.empty(N)


def X0(alpha):
    U = np.exp(-alpha * np.square(xaxis))
    return U


def init():
    global ax, wave, xaxis, yaxis
    # init the frame
    ax.set_xlim(-L, L)
    ax.set_ylim(-1.2,1.2)

    # init coord
    for i in range(N):
        xaxis[i] = ((2.0 * i - N + 1)/(N-1)) * L
    yaxis = X0(alpha)

    # intitate KdV equation
    init_kdv(yaxis, L/N, dt, esp)    

    wave.set_data(xaxis, yaxis)
    return wave,    


def update(frame):
    global yaxis
    yaxis = next_kdv(yaxis)
    wave.set_data(xaxis, yaxis)
    return wave,


wave, = plt.plot([], [], linewidth = 1.0, animated=True)
ani = an.FuncAnimation(fig, update, np.arange(1, 200),init_func=init, blit=True)
plt.show()


