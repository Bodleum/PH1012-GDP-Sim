import numpy as np
import time
import random
import os

from data.graphics_engine import GraphWin,color_rgb,Circle,Rectangle,Point,Image,Text,Line

from Ball import Ball
import data.constants as data
from Vector import *
import Wind

# Location
location = "St Andrews"  # St Andrews, Singapore or La Paz

st_results = {}

if input("Draw? (y/n) --> ") == "y":
    draw = True
else:
    draw = False

if input("Angle sweep? (y/n) --> ") == "y":
    sweep = True
else:
    sweep = False

tstep = 0.0075

def simulate(draw,tstep,results,vinit,location):
    # Save initial angle
    ang_init = vinit.degangle
    #List of objects in display
    disp_obj=[]

    #Create golf ball and set initial velocity
    golf=Ball(5,0,data.dragcoef,location)
    golf.addvel(vinit)

    if draw == True:
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
        for i in np.arange(data.flag_spacing,data.flag_range+1,data.flag_spacing):
            flag_i = Image(Point(data.distance_scale*i+13,data.ground_height-30),"./graphics/golf_flag.png")
            text_i = Text(Point(data.distance_scale*i+13,data.ground_height+40),str(i)+"m")
            text_i.setFill(color_rgb(255,255,255))
            flags.append(flag_i)
            flags.append(text_i)
            disp_obj.append(flag_i)
            disp_obj.append(text_i)

        # Location text
        loc_text = Text(Point(1000,100),location)
        loc_text.setFill(color_rgb(0,0,0))

        #Range text
        range_display = Text(Point(1000,250),"Distance: ")#+str(golf.x-5))
        range_display.setFill(color_rgb(0,0,0))

        # Max height display
        max_height_display = Text(Point(1000,275),"Max Height: ")
        max_height_display.setFill(color_rgb(0,0,0))

        # Wind arrow
        if location == "St Andrews":
            wind_arrow = Line(Point(1000, 200), Point(
                (1000-5*Wind.st_wind.x), (200+5*Wind.st_wind.y)))
            wind_text = Text(Point(1000, 165),
                             ("Wind:", round(Wind.st_wind.mag, 2), "m/s"))
        elif location == "La Paz":
            wind_arrow = Line(Point(1000, 200), Point(
                (1000-5*Wind.lp_wind.x), (200+5*Wind.lp_wind.y)))
            wind_text = Text(Point(1000, 165),
                            ("Wind:", round(Wind.lp_wind.mag, 2), "m/s"))
        elif location == "Singapore":
            wind_arrow = Line(Point(1000, 200), Point(
                (1000-5*Wind.s_wind.x), (200+5*Wind.s_wind.y)))
            wind_text = Text(Point(1000, 165),
                            ("Wind:", round(Wind.s_wind.mag, 2), "m/s"))
        
        wind_arrow.setWidth(1)
        wind_arrow.setArrow("last")
        

        #make window
        window = GraphWin("Golf Simulation", data.window_x, data.window_y)
        window.setBackground(color_rgb(124, 185, 232))

        #draw tee
        tee.draw(window)

        #draw clouds
        for i in clouds:
            i.draw(window)

        #draw golf ball
        golf_ball.draw(window)

        #draw ground
        ground.draw(window)

        #Draw Flags
        tee_text.draw(window)
        for i in flags:
            i.draw(window)

        # Draw Location text
        loc_text.draw(window)

        #Draw range and max height0 displays
        range_display.draw(window)
        max_height_display.draw(window)

        # Draw wind arrow
        wind_arrow.draw(window)
        wind_text.draw(window)

    def main_loop():

        scroll_vel = 0
        scroll = False
        model = True
        roll = False
        #Moving
        while model == True: #(golf.y)>=(data.ground_height) and (golf.inst_vel == None) or (golf.inst_vel.mag != 0):
            
            #Move golfball
            golf.update(tstep)

            if golf.y <= data.ground_height and roll == False:
                golf.bounce()
            
            if golf.inst_vel.mag <= 1 and roll == False:
                roll = True
                golf.roll()
            elif golf.inst_vel.mag <= 1 and roll == True:
                model = False

            if (data.distance_scale*golf.x) < 1000:
                scroll = False
            elif (data.distance_scale*golf.x) >= 1000:
                scroll = True
                scroll_vel = golf.inst_vel.x


            if draw == True:
                if scroll == False:
                    golf_ball.move(data.distance_scale*golf.xinc, -data.distance_scale*golf.yinc)
                    time.sleep(0.0025)
                elif scroll == True:
                    golf_ball.move(0, -data.distance_scale*golf.yinc)
                    for i in disp_obj:
                        i.move(data.distance_scale*(-scroll_vel*tstep), 0)
            
                #Move cloud
                for i in clouds:
                    if location == "St Andrews":
                        i.move(-1*Wind.st_wind.x*tstep, Wind.st_wind.y *
                               tstep + (random.uniform(-0.05, 0.05)))
                    elif location == "La Paz":
                        i.move(-1*Wind.lp_wind.x*tstep, Wind.lp_wind.y *
                                tstep + (random.uniform(-0.05, 0.05)))
                    elif location == "Singapore":
                        i.move(-1*Wind.s_wind.x*tstep, Wind.s_wind.y *
                               tstep + (random.uniform(-0.05, 0.05)))
                    
                #Update range and height displays
                range_display.setText("Distance: "+str(int(round(golf.x-5,3)))+"m") #-5
                max_height_display.setText("Max Height: "+str(int(round(golf.y_max, 3)))+"m")

        print("Done",ang_init)
        results[golf.x - 5] = ang_init

        os.remove("./logs/golf_ball_points.csv")
        points_file = open("./logs/golf_ball_points.csv","a")
        for i in range(0,len(golf.points)):
            points_file.write(str(golf.points[i][0])+","+str(golf.points[i][1])+"\n")
        points_file.close()

        if draw == True:
            Text(Point(1000,300),"Landed").draw(window)

            #Close window
            if sweep == False:
                window.getMouse()
            window.close()

    main_loop()


def dosweep(draw,tstep,results):
    for i in np.arange(data.sweep_start,data.sweep_end + 1,data.sweep_step):
        i = round(i,4)
        vinit = Vector("Vinit",data.hit_vel,i)
        simulate(draw,tstep,results,vinit,location)




if sweep == False:
    #Initial velocity
    v0 = float(input("Initial v? --> "))
    degangle = float(input("Angle? --> "))
    vinit = Vector("Vinit", v0, degangle)
    simulate(draw, tstep, st_results, vinit, location)
    print(st_results)

else:
    dosweep(draw,tstep,st_results)

    # top_3 = sorted(results.keys(),reverse=True)[:3]

    # print("----- Results -----")
    # for i,j in results.items():
    #     print("At",j,"degrees the golf ball traveled",round(i,5),"m.")
    print("----- Summary ("+str(location)+") -----")
    print("Top 3:")
    print("    1.",round(max(st_results.keys()),5),"m at",st_results[max(st_results.keys())],"degrees.")
    print("    2.", round(sorted(st_results.keys(), reverse=True)[1:2][0], 5), "m at", st_results[sorted(st_results.keys(), reverse=True)[1:2][0]],"degrees.")
    print("    3.", round(sorted(st_results.keys(), reverse=True)[2:3][0], 5), "m at", st_results[sorted(st_results.keys(), reverse=True)[2:3][0]], "degrees.")
# if self.loc == "St Andrews":
# elif self.loc == "La Paz":
# elif self.loc == "Singapore":
