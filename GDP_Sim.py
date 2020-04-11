import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from Ball import Ball
from data.constants import gravity
from Velocity import Velocity

v0 = float(input("Initial v? --> "))
degangle = float(input("Angle? --> "))
vinit = Velocity(v0,degangle)

#Drag Coefficient
dragcoef=float(input("Drag coefficient? (roughly 0.5) --> "))

#Time
tmax=(2*vinit.y/gravity)
tstep=0.1

#Range estimate
r_est=(vinit.x)*tmax

#Height extimate
h_est=(vinit.y**2)/(2*gravity)

#Graph data
x_data=[]
y_data=[]

golf=Ball(0,0,dragcoef)
golf.setvel(vinit)

fig, ax=plt.subplots()
ax.set_xlim(-2,1.1*r_est+5)
ax.set_ylim(-10,1.1*h_est+5)
line, =ax.plot(0,0)

def animation_frame(_):

    x_data.append(golf.x)  # Append to graph data
    y_data.append(golf.y)  # Append to graph data

    line.set_xdata(x_data)  # Add to line
    line.set_ydata(y_data)  # Add to line

    #Update golf
    golf.update(tstep)
    return line,

animation = FuncAnimation(fig,func=animation_frame,frames=np.arange(0,tmax,tstep),interval=1)
plt.show()
