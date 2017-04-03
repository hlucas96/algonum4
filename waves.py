import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an

fig, ax = plt.subplots()
L = 20.0
N = 100
alpha = 0.05

wave, = plt.plot([], [], linewidth = 1.0, animated=True)

xaxis = np.empty(N)
theta = np.empty(N)

def init():
    ax.set_xlim(-L, L)
    ax.set_ylim(0,1)
    for i in range(0, N, 1):
        xaxis[i] = ((2.0*i-N+1)/(N-1))*L
        theta[i] = np.exp(-alpha*np.square(xaxis[i]))
    wave.set_data(xaxis, theta)
    return wave,    
        
def update(frame):
    global alpha
    alpha = alpha + 0.05
    for i in range(0, N, 1):
        theta[i] = np.exp(-alpha*np.square(xaxis[i]))
    wave.set_data(xaxis, theta)
    return wave,

ani = an.FuncAnimation(fig, update, np.arange(1, 200),init_func=init, blit=True)

plt.show()    


