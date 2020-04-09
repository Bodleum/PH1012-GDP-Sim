import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Constants
gravity=9.81
airdens = 1.2041  # from Wikipedia -> temporary

#Initial conditions
v0=float(input("Initial v? --> "))
degangle=float(input("Angle? --> "))
radangle=(degangle*np.pi)/180
ux=v0*np.cos(radangle)
uy=v0*np.sin(radangle)

#Time
tmax=(2*v0*np.sin(radangle)/gravity)
print(tmax)
tstep=0.01

#Range estimate
r_est=(v0**2*np.sin(2*radangle))/gravity

#Height extimate
h_est=(v0**2*np.sin(radangle)**2)/(2*gravity)
class Ball:
    def __init__(self,x0,y0):

        #Mass and weight
        self.mass=0
        self.weight=self.mass*gravity

        #Radius and volume
        self.radius=0
        self.volume=(4/3)*np.pi*self.radius**3

        #x
        self.ax=0
        self.vx=0
        self.x=x0

        #y
        self.ay=0
        self.vy=0
        self.y=y0

        #Air resistance
        self.drag=0
        self.airres=self.drag*0.5*(np.pi*self.radius**2)*self.vx**2

    def update(self,t):

        #x
        self.ax=0
        self.vx=self.ax*t+ux
        self.x=0.5*self.ax*t**2+ux*t

        #y
        self.ay=-1*gravity
        self.vy=self.ay*t+uy
        self.y=0.5*self.ay*t**2+uy*t

        #Air resistance
        self.airres = self.drag*0.5*(np.pi*self.radius**2)*self.vx**2


golf=Ball(0,0)

x_data=[]
y_data=[]

fig, ax=plt.subplots()
ax.set_xlim(-2,1.1*r_est+5)
ax.set_ylim(-2,1.1*h_est+5)
line, =ax.plot(0,0)

def animation_frame(i):

    #Update golf
    golf.update(i)

    #Append to x_data and y_data
    x_data.append(golf.x)
    y_data.append(golf.y)

    #Add to line
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line,

animation = FuncAnimation(fig,func=animation_frame,frames=np.arange(0,tmax,tstep),interval=1)
plt.show()