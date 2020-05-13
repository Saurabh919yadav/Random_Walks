"""
    By using Numpy we can easil simulate a simple random walk.
    Given the number of steps N as an input argument, we can randomly generate N samples from the test set {+1, -1}
    with an equal probability of 0.5. Then we will only use the cumsum function, to give us the cumulative sum
    in every time step.
"""

import numpy as np
np.random.seed(1234)


def random_walk(N):
    """
    Simulates a discrete random walk
    : param int N : the numer of steps to take
    """

    # event space : set of posible increments
    increments = np.array([1, -1])
    # the probability to generate any element
    p = 0.5

    # selecting values
    random_increments = np.random.choice(increments, N, p)

    # calculating random walk
    random_walk = np.cumsum(random_increments)

    return random_walk, random_increments


# generate a random walk
N = 500
X, epsilon = random_walk(N)


# normalizing the random walk using the Central Limit Theoram
X = X*np.sqrt(1./N)



import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure(figsize= (20, 10))
ax = plt.axes(xlim= (0, N), ylim= (np.min(X)-0.5, np.max(X)+0.5))
line, = ax.plot([], [], lw= 2, color= 'red')
ax.set_xticks(np.arange(0, N+1, 50))
ax.set_yticks(np.arange(np.min(X)-0.5, np.max(X)+0.5, 0.2))
ax.set_title("Simple 1D random walk", fontsize= 22)
ax.set_xlabel('Steps', fontsize= 18)
ax.set_ylabel('Value', fontsize= 18)
ax.tick_params(labelsize= 16)
ax.grid(True, which= 'major', linestyle= '--', color= 'black', alpha= 0.4)


# initialization function
def init():
    # creating empty plot/frame
    line.set_data([],[])
    return line,

# List to store x and y points
xdata, ydata = [], []

# animation function

def animate(i):
    y = X[i]
    xdata.append(i)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line,

# call the animator
anim = animation.FuncAnimation(fig, animate, init_func=init, frames= N, interval =20, blit= True)
# anim.save('random_walk.gif')  *error : movie writter not available
