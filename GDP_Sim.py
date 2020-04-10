import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from Velocity import *
from Ball import Ball
from data.constants import gravity

#Initial conditions
v0=float(input("Initial v? --> "))
degangle=float(input("Angle? --> "))
radangle=(degangle*np.pi)/180
vinit=Velocity(v0,degangle)

#Drag Coefficient
dragcoef=float(input("Drag coefficient? (roughly 0.5) --> "))

#Time
tmax=(2*v0*np.sin(radangle)/gravity)
tstep=0.1

#Range estimate
r_est=(v0**2*np.sin(2*radangle))/gravity

#Height extimate
h_est=(v0**2*np.sin(radangle)**2)/(2*gravity)

#Graph data
x_data=[]
y_data=[]

golf=Ball(0,0,dragcoef)

fig, ax=plt.subplots()
ax.set_xlim(-2,1.1*r_est+5)
ax.set_ylim(-2,1.1*h_est+5)
line, =ax.plot(0,0)

def animation_frame(i):

    #Update golf
    golf.update(i)

    line.set_xdata(x_data)  # Add to line
    line.set_ydata(y_data)  # Add to line
    return line,

animation = FuncAnimation(fig,func=animation_frame,frames=np.arange(0,tmax,tstep),interval=1)
plt.show()
