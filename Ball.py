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
        self.vel_dict={}

        #Acceleration
        self.accel = None
        self.accel_dict={}
        self.addaccel(Vector("Gravity", data.gravity, -90))

    def addvel(self,vel2):
        self.vel_dict[vel2.name] = vel2

    def addaccel(self,accel2):
        self.accel_dict[accel2.name] = accel2

    def update(self, tstep):

        #Lists
        self.accel_list = list(self.accel_dict.values())
        self.vel_list = list(self.vel_dict.values())

        #Acceleration
        self.accel = self.accel_list[0]
        if len(self.accel_list)>1:
            for i in range(1,len(self.accel_list)):
                self.accel.add(self.accel_list[i])

        #Velocity
        self.vel = self.vel_list[0]
        self.addvel(Vector("Velocity_step",self.accel.mag*tstep,self.accel.degangle))
        if len(self.vel_list)>1:
            for i in range(1,len(self.vel_list)):
                self.vel.add(self.vel_list[i])

        #Increase
        self.xinc = self.vel.x*tstep
        self.yinc = self.vel.y*tstep

        #Position
        self.x += self.xinc
        self.y += self.yinc

        #Air resistance
        # self.addaccel(Vector("Air_resistance", ((data.airdens*self.drag * 0.5*(np.pi*self.radius**2)*self.vel.mag**2)/self.mass), (self.vel.degangle-180)))
        