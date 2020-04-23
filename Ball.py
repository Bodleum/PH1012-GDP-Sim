import numpy as np
import random

import data.constants as data
from Vector import *
import Wind

class Ball:
    def __init__(self, x0, y0,dragcoef,location):

        self.loc = location

        #Mass and weight
        self.mass = data.golf_ball_mass
        if self.loc == "St Andrews":
            self.weight = self.mass*data.st_gravity
        elif self.loc == "La Paz":
            self.weight = self.mass*data.lp_gravity
        elif self.loc == "Singapore":
            self.weight = self.mass*data.s_gravity

        #Radius and volume
        self.radius = data.golf_ball_radius
        self.vradius=self.radius*data.radius_scale#NOT IN METERS

        #x
        self.x = x0

        #y
        self.y = y0 + (data.ground_height)
        self.y_max = y0 - data.ground_height

        self.points = []

        #Air resistance
        self.drag = dragcoef

        #Velocity
        self.inst_vel=None
        self.vel_dict={}

        #Acceleration
        self.inst_accel = None
        self.accel_dict={}
        if self.loc == "St Andrews":
            self.addaccel(Vector("Gravity", data.st_gravity, -90))
        elif self.loc == "La Paz":
            self.addaccel(Vector("Gravity", data.lp_gravity, -90))
        elif self.loc == "Singapore":
            self.addaccel(Vector("Gravity", data.s_gravity, -90))

        # Wind
        self.wind_rel = None

    def addvel(self,vel2):
        self.vel_dict[vel2.name] = vel2

    def addaccel(self,accel2):
        self.accel_dict[accel2.name] = accel2

    def update(self, tstep, wind):

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
        if self.y_max < (self.y-data.ground_height):
            self.y_max = self.y - data.ground_height
        
        self.points.append([round(self.x-5,3),round(self.y-data.ground_height,3)])

        # Wind
        self.wind_rel = Vector("Wind_rel",self.inst_vel.mag,self.inst_vel.degangle)
        if self.loc == "St Andrews":
            self.wind_rel.add(wind)
        elif self.loc == "La Paz":
            self.wind_rel.add(wind)
        elif self.loc == "Singapore":
            self.wind_rel.add(wind)

        #Reset acceleration
        self.inst_accel = None
        self.accel_dict = {}

        if self.y > data.ground_height+1:
            #Gravity
            if self.loc == "St Andrews":
                self.addaccel(Vector("Gravity", data.st_gravity, -90))
            elif self.loc == "La Paz":
                self.addaccel(Vector("Gravity", data.lp_gravity, -90))
            elif self.loc == "Singapore":
                self.addaccel(Vector("Gravity", data.s_gravity, -90))
            

            #Air resistance
            if self.loc == "St Andrews":
                self.addaccel(Vector("Air_resistance", ((data.st_airdens*self.drag * 0.5*(
                    np.pi*self.radius**2)*self.wind_rel.mag**2)/self.mass), (self.wind_rel.degangle-180)))
            elif self.loc == "La Paz":
                self.addaccel(Vector("Air_resistance", ((data.lp_airdens*self.drag * 0.5*(
                    np.pi*self.radius**2)*self.wind_rel.mag**2)/self.mass), (self.wind_rel.degangle-180)))
            elif self.loc == "Singapore":
                self.addaccel(Vector("Air_resistance", ((data.s_airdens*self.drag * 0.5*(
                    np.pi*self.radius**2)*self.wind_rel.mag**2)/self.mass), (self.wind_rel.degangle-180)))

            # Spin
            if self.loc == "St Andrews":
                self.addaccel(Vector("Spin_lift", (0.5*data.liftcoef*data.st_airdens*(
                    np.pi*self.radius**2)*self.wind_rel.mag**2)/self.mass, (self.wind_rel.degangle+90)))
            elif self.loc == "La Paz":
                self.addaccel(Vector("Spin_lift",(0.5*data.liftcoef*data.lp_airdens*(
                    np.pi*self.radius**2)*self.wind_rel.mag**2)/self.mass,(self.wind_rel.degangle+90)))
            elif self.loc == "Singapore":
                self.addaccel(Vector("Spin_lift", (0.5*data.liftcoef*data.s_airdens*(
                    np.pi*self.radius**2)*self.wind_rel.mag**2)/self.mass, (self.wind_rel.degangle+90)))

        # Roll friction
        if self.y <= data.ground_height+1:
            if self.loc == "St Andrews":
                self.addaccel(Vector("Ground_friction",data.st_gravity*data.friccoef,self.inst_vel.degangle - 180))
            elif self.loc == "La Paz":
                self.addaccel(Vector("Ground_friction",data.lp_gravity*data.friccoef,self.inst_vel.degangle - 180))
            elif self.loc == "Singapore":
                self.addaccel(Vector("Ground_friction",data.s_gravity*data.friccoef,self.inst_vel.degangle - 180))
            
            
            round(self.inst_vel.mag,3)
        

    def bounce(self):
        if data.cor*self.inst_vel.mag >= 1:
            self.y = data.ground_height + 0.5
            temp = Vector("Bounce_velocity",data.cor*self.inst_vel.mag,-1*self.inst_vel.degangle)
            self.inst_vel=None
            self.vel_dict = {}
            self.addvel(temp)
            self.inst_vel = temp
        elif self.inst_vel.mag < 1:
            self.inst_vel.mag = 0

    def roll(self):
        temp = Vector("Roll",1,0)
        self.inst_vel = None
        self.vel_dict = {}
        self.addvel(temp)
        self.inst_vel = temp
        self.y = data.ground_height
