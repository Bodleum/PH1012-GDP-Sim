import numpy as np
import time
import random

from data.graphics_engine import GraphWin,color_rgb,Circle,Rectangle,Point,Image,Text

from Ball import Ball
import data.constants as data
from Velocity import Velocity

#List of objects in display
disp_obj=[]
scroll_vel=0

#Initial velocity
v0 = float(input("Initial v? --> "))
degangle = float(input("Angle? --> "))
vinit = Velocity(v0,degangle)

#Drag Coefficient
dragcoef=0.47 #float(input("Drag coefficient? (roughly 0.5) --> "))

#Time
tmax = (2*vinit.y/data.gravity)
tstep=0.0025

#Range and height estimates
range_est=(vinit.x)*tmax
height_est = (vinit.y**2)/(2*data.gravity)

#Create golf ball and set initial velocity
golf=Ball(5,0,dragcoef)
golf.setvel(vinit)

#Make golf ball
golf_ball=Circle(Point(golf.x+golf.vradius,golf.y-golf.vradius),golf.vradius)
golf_ball.setFill(color_rgb(240,248,255))
golf_ball.setWidth(0)
# Not in disp_obj

#Make tee
tee = Image(Point(7.5, data.ground_height-1), "./graphics/tee.png")
disp_obj.append(tee)
tee_text = Text(Point(12, data.ground_height+40), "0m")
tee_text.setFill(color_rgb(255,255,255))
disp_obj.append(tee_text)


#Make ground
grounds=[]
for i in np.arange(25,2500,50):
    ground_i=Image(Point(i,data.ground_height+40),"./graphics/grass.png")
    grounds.append(ground_i)
    disp_obj.append(ground_i)

#Make cloud
clouds=[]
for i in range(0,random.randint(1,2)):
    cloud_start_x = random.randint(100,0.8*data.window_x)
    cloud_start_y = random.randint(0,300)
    cloud_i = Image(Point(cloud_start_x, cloud_start_y),"./graphics/cloud_"+str(random.randint(1,11))+".png")
    clouds.append(cloud_i)
    disp_obj.append(cloud_i)

#Flags
flags=[]
for i in np.arange(50,int(2500/data.distance_scale),50):
    flag_i = Image(Point(data.distance_scale*i+13,data.ground_height-30),"./graphics/golf_flag.png")
    text_i = Text(Point(data.distance_scale*i+13,data.ground_height+40),str(i)+"m")
    text_i.setFill(color_rgb(255,255,255))
    flags.append(flag_i)
    flags.append(text_i)
    disp_obj.append(flag_i)
    disp_obj.append(text_i)

#Range text
range_display = Text(Point(1100,250),"Distance: ")#+str(golf.x-5))
range_display.setFill(color_rgb(0,0,0))

def main_loop():
    #Moving
    while (golf.y)>=(data.ground_height):

        #Move cloud
        for i in clouds:
            i.move(0.02,(random.uniform(-0.05,0.05)))
        
        #Move golfball
        golf.update(tstep)
        if (golf.x*data.distance_scale) <= 1000:
            golf_ball.move(data.distance_scale*golf.xinc, -data.distance_scale*golf.yinc)
        else:
            scroll_vel=-data.distance_scale**3*golf.vel.x
            for i in disp_obj:
                i.move(scroll_vel*data.distance_scale*tstep,0)
                golf_ball.move(0, -data.distance_scale*golf.yinc)


        #Update range display
        range_display.setText("Distance: "+str(int(round(golf.x-5,1)))+"m")

    #Close window
    window.getMouse()
    window.close()

#make window
window = GraphWin("Golf Simulation", data.window_x, data.window_y)
window.setBackground(color_rgb(124, 185, 232))

#draw tee
tee.draw(window)

#draw golf ball
golf_ball.draw(window)

#draw ground
for i in grounds:
    i.draw(window)

#draw clouds
for i in clouds:
    i.draw(window)

#Draw Flags
tee_text.draw(window)
for i in flags:
        i.draw(window)

#Draw range display
range_display.draw(window)

main_loop()
