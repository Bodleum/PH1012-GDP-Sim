import numpy as np

class Vector:

    def __init__(self,name,mag,degangle):
        self.name=name
        self.mag = mag
        if degangle > 180:
            self.degangle = degangle -360
        elif degangle <= -180:
            self.degangle = degangle + 360
        else:
            self.degangle = degangle
        self.resolve()

    def resolve(self):
        self.radangle = (self.degangle*np.pi)/180
        self.x = self.mag*np.cos(self.radangle)
        self.y = self.mag*np.sin(self.radangle)

        self.quad()

    def quad(self):
        if 0 <= self.degangle and 90 >= self.degangle:  # Quad 1
            self.x = np.abs(self.x)
            self.y = np.abs(self.y)
        elif 90 < self.degangle and 180 >= self.degangle:  # Quad 2
            self.x = -1*np.abs(self.x)
            self.y = np.abs(self.y)
        elif -90 > self.degangle and -180 < self.degangle:  # Quad 3
            self.x = -1*np.abs(self.x)
            self.y = -1*np.abs(self.y)
        elif 0 > self.degangle and -90 <= self.degangle:  # Quad
            self.x = np.abs(self.x)
            self.y = -1*np.abs(self.y)

    def add(self,vec2):
        self.name = str(self.name+" + "+vec2.name)

        self.x += vec2.x
        self.y += vec2.y

        self.mag = np.sqrt(self.x**2+self.y**2)
        self.radangle = np.arctan2(self.y, self.x)
        self.degangle = self.radangle * 180/np.pi

        self.quad()
        
    def rename(self,rename):
        self.name = rename
