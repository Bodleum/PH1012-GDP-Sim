import numpy as np

class Acceleration:
    
    def __init__(self,name,mag,degangle):
        self.name=name
        self.mag = mag
        self.degangle = degangle

    def resolve(self):
        self.radangle = (self.degangle*np.pi)/180
        self.x = self.mag*np.cos(self.radangle)
        self.y = self.mag*np.sin(self.radangle)

    def add(self, accel2):
        self.mag += accel2.mag
        self.degangle += accel2.degangle
        if self.degangle > 180:
            self.degangle += -360
        elif self.degangle <= (-180):
            self.degangle += 360

        self.resolve()

    def rename(self, rename):
        self.name = rename
