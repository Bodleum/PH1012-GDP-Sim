import numpy as np

import data.constants as data
from Vector import *

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

        #Velocity
        self.vel=None

        #Acceleration
        self.accel=None

    def addvel(self,name,mag,angle):
        if self.vel==None:
            self.vel = (Vector(name,mag,angle))
        else:
            self.vel.add(Vector(name,mag,angle))

    def veladdvel(self,vel2):
        if self.vel == None:
            self.vel = vel2
        else:
            self.vel.add(vel2)

    def addaccel(self,name,mag,angle):
        if self.accel==None:
            self.accel = (Vector(name,mag,angle))
        else:
            self.accel.add(Vector(name,mag,angle))

    def acceladdaccel(self,accel2):
        if self.accel == None:
            self.accel = accel2
        else:
            self.accel.add(accel2)

    def update(self, tstep):

        #Reset acceleration with gravity
        self.accel = Vector("Gravity",data.gravity,-90)

        #Air resistance
        self.air_resistance = Vector("Air_resistance", (data.airdens*self.drag * 0.5*(np.pi*self.radius**2)*self.vel.mag**2/self.mass),self.vel.degangle-180)

        #Acceleration
        self.acceladdaccel(self.air_resistance)

        #Velocity
        self.addvel("Velocity_step",self.accel.mag*tstep,self.accel.degangle)

        #Increase
        self.xinc = self.vel.x*tstep
        self.yinc = self.vel.y*tstep

        #Position
        self.x += self.xinc
        self.y += self.yinc