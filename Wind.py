import numpy as np
import random
from Vector import *
import data.constants as data

if data.random_wind == True:

    def pm():
        return 180 if random.random() < 0.5 else 0

    st_wind = Vector("Wind", np.random.normal(data.st_wind_avg, 1),random.uniform(-35, 35)-pm())

    lp_wind = Vector("Wind", np.random.normal(data.lp_wind_avg, 1), random.uniform(-35, 35)-pm())

    s_wind = Vector("Wind", np.random.normal(data.s_wind_avg, 1), random.uniform(-35, 35)-pm())
else:
    wind = Vector("Wind",data.fixed_wind_mag,data.fixed_wind_angle + 180)
