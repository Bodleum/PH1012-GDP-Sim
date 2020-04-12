import numpy as np
import time
import random

from data.graphics_engine import GraphWin,color_rgb,Circle,Rectangle,Point,Image,Text

from Ball import Ball
import data.constants as data
from Velocity import Velocity

#Initial velocity
v0 = float(input("Initial v? --> "))
degangle = float(input("Angle? --> "))
vinit = Velocity(v0,degangle)

#Drag Coefficient
dragcoef=0.47 #float(input("Drag coefficient? (roughly 0.5) --> "))

#Time
tmax = (2*vinit.y/data.gravity)
tstep=0.001

#Range and height estimates
range_est=(vinit.x)*tmax
height_est = (vinit.y**2)/(2*data.gravity)

#Create golf ball and set initial velocity
golf=Ball(0,0,dragcoef)
golf.setvel(vinit)

#Make golf ball
golf_ball=Circle(Point(golf.x+golf.vradius,golf.y-golf.vradius),golf.vradius)
golf_ball.setFill(color_rgb(240,248,255))
golf_ball.setWidth(0)

#Make ground
ground=Rectangle(Point(-10,(data.window_y+10)),Point((data.window_x+10),(data.distance_scale*data.ground_height+5)))
ground.setFill(color_rgb(84,45,36))
ground.setOutline(color_rgb(125,194,66))
ground.setWidth(10)

#Make cloud
cloud_start = random.randint(100,0.8*data.window_x)
cloud=Rectangle(Point(cloud_start,125),Point((cloud_start+300),50))
cloud = Image(Point(cloud_start, 125),"./graphics/cloud_"+str(random.randint(1,11))+".png")

#Flags
flags=[]
for i in np.arange(50,int(data.window_x/data.distance_scale),50):
    flag_i = Image(Point(data.distance_scale*i,data.distance_scale*data.ground_height-30),"./graphics/golf_flag.png")
    text_i = Text(Point(data.distance_scale*i,data.distance_scale*data.ground_height+20),str(i)+"m")
    text_i.setFill(color_rgb(255,255,255))
    flags.append(flag_i)
    flags.append(text_i)

print(flags)
# flag=Image(Point(data.distance_scale*50,data.distance_scale*data.ground_height-30),"./graphics/golf_flag.png")

def main():

    #make window
    window=GraphWin("Golf Simulation",data.window_x,data.window_y)
    window.setBackground(color_rgb(124,185,232))

    #draw
    golf_ball.draw(window)
    ground.draw(window)
    cloud.draw(window)
    for i in flags:
        i.draw(window)

    #Moving
    while (golf.y)>=(data.distance_scale*data.ground_height):
        #Move cloud
        cloud.move(0.02,(random.uniform(-0.05,0.05)))
        
        #Move golfball
        golf.update(tstep)
        golf_ball.move(data.distance_scale*golf.xinc, -data.distance_scale*golf.yinc)

    #Close window
    window.getMouse()
    window.close()

main()
