import plotly.graph_objects as go
import numpy as np
np.random.seed(1)

l = 1000
x_steps = np.random.choice([-1,1], size=l) + 0.2 * np.random.randn(l) # L steps
y_steps = np.random.choice([-1,1], size=l) + 0.2 * np.random.randn(l) # L steps
x_position = np.cumsum(x_steps) # integrate the position by summing steps values
y_position = np.cumsum(y_steps) # integrate the position by summing steps values

fig = go.Figure(data= go.Scatter(
    x= x_position,
    y= y_position,
    mode= 'markers',
    name= ' Random Walk in 1D',
    marker= dict(
        color= np.arange(l),
        size= 8,
        colorscale= 'Greens',
        showscale= True
    )

))

fig.show()