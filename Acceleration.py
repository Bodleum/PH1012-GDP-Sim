import numpy as np

class Acceleration:
    
    def __init__(self,name,mag,degangle):
        self.name=name
        self.mag = mag
        self.degangle = degangle
        self.radangle = (self.degangle*np.pi)/180
        self.x = self.mag*np.cos(self.radangle)
        self.y = self.mag*np.sin(self.radangle)