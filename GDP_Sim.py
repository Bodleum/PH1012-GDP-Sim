import numpy as np
import time
import random

from data.graphics_engine import GraphWin,color_rgb,Circle,Rectangle,Point,Image,Text

from Ball import Ball
import data.constants as data
from Vector import *

#List of objects in display
disp_obj=[]
scroll_vel=0
scroll = False

#Initial velocity
v0 = float(input("Initial v? --> "))
degangle = float(input("Angle? --> "))
vinit = Vector("Vinit", v0, degangle)

#Time
tmax = (2*vinit.y/data.gravity)
tstep=0.0025

#Range and height estimates
range_est=(vinit.x)*tmax
height_est = (vinit.y**2)/(2*data.gravity)

#Create golf ball and set initial velocity
golf=Ball(5,0,data.dragcoef)
golf.addvel(vinit)

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
ground = Image(Point(6400,data.ground_height+40),"./graphics/grass_long.png")
disp_obj.append(ground)

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
for i in np.arange(50,int(501),50):
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
        if (data.distance_scale*golf.x) < 1000:
            scroll = False
        elif (data.distance_scale*golf.x) >= 1000:
            scroll = True
            scroll_vel = golf.inst_vel.x

        if scroll == False:
            golf_ball.move(data.distance_scale*golf.xinc, -data.distance_scale*golf.yinc)
        elif scroll == True:
            golf_ball.move(0, -data.distance_scale*golf.yinc)
            for i in disp_obj:
                i.move(data.distance_scale*(-scroll_vel*tstep), 0)
        

        #Update range displays
        range_display.setText("Distance: "+str(int(round(golf.x-5,3)))+"m")

    print("Done")

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
ground.draw(window)

#draw clouds
for i in clouds:
    i.draw(window)

#Draw Flags
tee_text.draw(window)
for i in flags:j
        i.draw(window)

#Draw range display
range_display.draw(window)

main_loop()
