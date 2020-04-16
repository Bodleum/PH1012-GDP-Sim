import numpy as np
import random
from Vector import *
import data.constants as data

def pm():
    return 180 if random.random() < 0.5 else 0

wind = Vector("Wind", np.random.normal(data.wind_avg, 1),random.uniform(-35, 35)-pm())