import numpy as np

import data.constants as data

class Ball:
    def __init__(self, x0, y0,dragcoef):

        #Mass and weight
        self.mass = data.golf_ball_mass
        self.weight = -1*self.mass*data.gravity

        #Radius and volume
        self.radius = data.golf_ball_radius
        self.vradius=self.radius*data.radius_scale#NOT IN METERS

        #x
        self.x = x0

        #y
        self.y = y0 + (data.ground_height)

        #Air resistance
        self.drag = dragcoef

    def setvel(self, velocity):
        self.vel = velocity

    def update(self, tstep):

        #Air resistance
        self.airresx = -1*data.airdens*self.drag *0.5*(np.pi*self.radius**2)*self.vel.x**2
        self.airresy = -1*data.airdens*self.drag *0.5*(np.pi*self.radius**2)*self.vel.y**2

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
