import numpy as np

from data.constants import *

#Graph data
x_data = []
y_data = []

class Ball:
    def __init__(self, x0, y0,dragcoef):

        #Mass and weight
        self.mass = 0.05
        self.weight = -1*self.mass*gravity

        #Radius and volume
        self.radius = 0.02
        self.volume = (4/3)*np.pi*self.radius**3

        #x
        self.ax = 0
        self.x = x0

        #y
        self.ay = 0
        self.y = y0

        self.vel = 0

        #Air resistance
        self.drag = dragcoef
        self.airresx = 0
        self.airresy = 0

    def setvel(self, velocity):
        self.vel = velocity

    def update(self, t):

        #x
        self.ax = (self.airresx/self.mass)
        self.vel.x += self.ax
        self.x += self.vel.x

        #y
        self.ay = -1*gravity + (self.airresy/self.mass)
        self.vel.y += self.ay
        self.y += self.vel.y

        #Air resistance
        self.airresx = -1*airdens*self.drag *0.5*(np.pi*self.radius**2)*self.vel.x**2
        self.airresy = -1*airdens*self.drag *0.5*(np.pi*self.radius**2)*self.vel.y**2

        #Set ux and uy for next update
        # self.ux=self.vx
        # self.uy=self.vy
