import numpy as np
import time

from data.graphics import GraphWin,color_rgb,Circle,Rectangle,Point

from Ball import Ball
import data.constants as data
from Velocity import Velocity

v0 = float(input("Initial v? --> "))
degangle = float(input("Angle? --> "))
vinit = Velocity(v0,degangle)

#Drag Coefficient
dragcoef=0.47 #float(input("Drag coefficient? (roughly 0.5) --> "))

#Time
tmax = (2*vinit.y/data.gravity)
tstep=0.001

#Range estimate
r_est=(vinit.x)*tmax

#Height extimate
h_est = (vinit.y**2)/(2*data.gravity)

#Graph data
x_data=[]
y_data=[]

golf=Ball(0,0,dragcoef)
golf.setvel(vinit)

#create golf ball
golf_ball=Circle(Point(golf.x+golf.vradius,golf.y-golf.vradius),golf.vradius)
golf_ball.setFill(color_rgb(255,255,255))

#make ground
ground=Rectangle(Point(0,700),Point(1200,560))
ground.setFill(color_rgb(0,255,0))

def main():

    #make window
    window=GraphWin("Golf Simulation",1200,700)
    window.setBackground(color_rgb(0,0,0))

    #draw
    golf_ball.draw(window)
    ground.draw(window)

    #moving golf ball
    while (golf.y)>=(560):
        # print(golf.y)
        golf.update(tstep)
        golf_ball.move(data.distance_scale*golf.xinc, -data.distance_scale*golf.yinc)
        # time.sleep(0.01*tstep)

    #close window
    window.getMouse()
    window.close()

main()
