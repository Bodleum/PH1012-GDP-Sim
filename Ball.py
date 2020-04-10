import numpy as np

from GDP_Sim import gravity,airdens,vinit,x_data,y_data 

class Ball:
    def __init__(self, x0, y0,dragcoef):

        #Mass and weight
        self.mass = 0.05
        self.weight = -1*self.mass*gravity

        #Radius and volume
        self.radius = 0.02
        self.volume = (4/3)*np.pi*self.radius**3

        #x
        self.ax = None
        self.vx = None
        self.x = x0

        #y
        self.ay = None
        self.vy = None
        self.y = y0

        #Initial velocities
        self.ux = vinit.x
        self.uy = vinit.y

        #Air resistance
        self.drag = dragcoef
        self.airresx = airdens*self.drag*0.5*(np.pi*self.radius**2)*self.vx**2
        self.airresy = airdens*self.drag*0.5*(np.pi*self.radius**2)*self.vy**2

    def update(self, t):

        #x
        self.ax = (self.airresx/self.mass)
        self.vx = self.ax*t+self.ux
        self.x = 0.5*self.ax*t**2+self.ux*t
        x_data.append(self.x)  # Append to graph data

        #y
        self.ay = -1*gravity + (self.airresy/self.mass)
        self.vy = self.ay*t+self.uy
        self.y = 0.5*self.ay*t**2+self.uy*t
        y_data.append(self.y)  # Append to graph data

        #Air resistance
        self.airresx = -1*airdens*self.drag * \
            0.5*(np.pi*self.radius**2)*self.vx**2
        self.airresy = -1*airdens*self.drag * \
            0.5*(np.pi*self.radius**2)*self.vy**2

        #Set ux and uy for next update
        # self.ux=self.vx
        # self.uy=self.vy
