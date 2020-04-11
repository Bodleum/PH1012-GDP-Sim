import numpy as np

from data.graphics import *

from Ball import Ball
from data.constants import gravity
from Velocity import Velocity

v0 = float(input("Initial v? --> "))
degangle = float(input("Angle? --> "))
vinit = Velocity(v0,degangle)

#Drag Coefficient
dragcoef=float(input("Drag coefficient? (roughly 0.5) --> "))

#Time
tmax=(2*vinit.y/gravity)
tstep=0.1

#Range estimate
r_est=(vinit.x)*tmax

#Height extimate
h_est=(vinit.y**2)/(2*gravity)

#Graph data
x_data=[]
y_data=[]

golf=Ball(0,0,dragcoef)
golf.setvel(vinit)
