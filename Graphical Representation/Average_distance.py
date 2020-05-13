import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


l = 1000
N = 10000
t = np.arange(l)
steps = np.random.choice([-1, 1], size=(N, l)) + 0.05*np.random.standard_normal((N, l)) # L steps
position = np.cumsum(steps, axis= 1)
average_distance = np.std(position, axis=0)


fig = make_subplots(1, 2)
fig.add_trace(go.Scatter(x= t, y= average_distance, name= 'mean distance'), 1, 1)
fig.add_trace(go.Scatter(x= t, y= average_distance**2, name= 'mean squared distance'), 1, 2)
fig.update_xaxes(title_text= '$t$')
fig.update_yaxes(title_text= '$l$', col= 1)
fig.update_yaxes(title_text= '$l^2$', col= 2)
fig.update_layout(showlegend= False)
fig.show()
