import numpy as np

import data.constants as data

#Graph data
x_data = []
y_data = []

class Ball:
    def __init__(self, x0, y0,dragcoef):

        #Mass and weight
        self.mass = 0.05
        self.weight = -1*self.mass*data.gravity

        #Radius and volume
        self.radius = 0.02 
        self.vradius=self.radius*data.radius_scale#NOT IN METERS
        self.volume = (4/3)*np.pi*self.radius**3

        #x
        self.ax = 0
        self.x = x0

        #y
        self.ay = 0
        self.y = y0 + 560

        self.vel = 0

        #Air resistance
        self.drag = dragcoef
        self.airresx = 0
        self.airresy = 0

    def setvel(self, velocity):
        self.vel = velocity

    def update(self, tstep):

        #x
        self.ax = (self.airresx/self.mass)
        self.vel.x += self.ax*tstep
        self.x += self.vel.x*tstep
        self.xinc = self.vel.x*tstep

        #y
        self.ay = -1*data.gravity + (self.airresy/self.mass)
        self.vel.y += self.ay*tstep
        self.y += self.vel.y*tstep
        self.yinc = self.vel.y*tstep

        #Air resistance
        self.airresx = -1*data.airdens*self.drag *0.5*(np.pi*self.radius**2)*self.vel.x**2
        self.airresy = -1*data.airdens*self.drag * \
            0.5*(np.pi*self.radius**2)*self.vel.y**2

        #Set ux and uy for next update
        # self.ux=self.vx
        # self.uy=self.vy
