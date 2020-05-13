"""
    We compute a large number N of random walks representing for examples molecules in a small drop of chemical.
    While all the trajectories start at 0, after some time the spaial distribution of points is a Gaussian distribution
"""
import plotly.graph_objects as go
import numpy as np

l = 1000
N = 10000

steps = np.random.choice([-1, 1], size=(N, l)) + 0.05*np.random.standard_normal((N, l)) # L steps
position = np.cumsum(steps, axis= 1)

fig = go.Figure(data = go.Histogram(x= position[:, -1]))
fig.show()