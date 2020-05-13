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