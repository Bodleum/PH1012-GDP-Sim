import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

gravity=9.81
airdens = 1.2041  # from Wikipedia -> temporary
t=0
tmax=float(input("Maximum time? --> "))
tstep=0.01
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
        self.vx=self.ax*t
        self.x=0.5*self.ax*t**2

        #y
        self.ay=-1*gravity
        self.vy=self.ay*t
        self.y=0.5*self.ay*t**2

        #Air resistance
        self.airres = self.drag*0.5*(np.pi*self.radius**2)*self.vx**2
        
