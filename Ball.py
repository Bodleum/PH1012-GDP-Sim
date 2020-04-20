import numpy as np
import random

import data.constants as data
from Vector import *
import Wind

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
        self.inst_vel=None
        self.vel_dict={}

        #Acceleration
        self.inst_accel = None
        self.accel_dict={}
        self.addaccel(Vector("Gravity", data.gravity, -90))

        # Wind
        self.wind_rel = None

        # Spin
        self.w = None

    def addvel(self,vel2):
        self.vel_dict[vel2.name] = vel2

    def addaccel(self,accel2):
        self.accel_dict[accel2.name] = accel2

    def update(self, tstep):

        #Lists
        self.accel_list = list(self.accel_dict.values())
        self.vel_list = list(self.vel_dict.values())

        #Acceleration
        self.inst_accel = self.accel_list[0]
        if len(self.accel_list) > 1:
            for i in range(1,len(self.accel_list)):
                self.inst_accel.add(self.accel_list[i])

        #Velocity
        self.inst_vel = self.vel_list[0]
        self.addvel(Vector("Velocity_step",self.inst_accel.mag*tstep,self.inst_accel.degangle))
        if len(self.vel_list)>1:
            for i in range(1,len(self.vel_list)):
                self.inst_vel.add(self.vel_list[i])

        #Increase
        self.xinc = self.inst_vel.x*tstep
        self.yinc = self.inst_vel.y*tstep

        #Position
        self.x += self.xinc
        self.y += self.yinc

        # Wind
        self.wind_rel = Vector("Wind_rel",self.inst_vel.mag,self.inst_vel.degangle)
        self.wind_rel.add(Wind.wind)

        #Reset acceleration
        self.inst_accel = None
        self.accel_dict = {}

        #Gravity
        self.addaccel(Vector("Gravity", data.gravity, -90))

        #Air resistance
        self.addaccel(Vector("Air_resistance", ((data.airdens*self.drag * 0.5*(np.pi*self.radius**2)*self.wind_rel.mag**2)/self.mass), (self.wind_rel.degangle-180)))

        # Spin
        self.addaccel(Vector("Spin_lift",(0.5*data.liftcoef*data.airdens*(np.pi*self.radius**2)*self.wind_rel.mag**2)/self.mass,(self.wind_rel.degangle+90)))
        
