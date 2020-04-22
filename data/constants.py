import numpy as np

# Angle sweep
sweep_start = 5 # Angle to start sweep at in degrees
sweep_end = 45 # Angle to end sweep at in degrees
sweep_step = 1 # Angl sweep step in degrees

# Visual
radius_scale = 150 # Multiplier to artificially inflate the golf ball's size, bigger means larger ball
                   # VISUAL ONLY
distance_scale = 3.5 # Multiplier for how zoomed in/out the scene is, bigger means more zoomed in
ground_height = 620 # How high the ground is in pixels, reccomend not changing
flag_spacing = 50 # Distance between flags in m
flag_range = 400 # Furthest out flag marker in m


# Golf ball
golf_ball_mass = 0.05 # Mass of golf ball in kg
golf_ball_radius = 0.02 # Radius of golfball in m
dragcoef = 0.47 # Drag coefficient of golf ball, larger means more air resistance, 0 is no air resistance
liftcoef = (2.5/3.5)*dragcoef
cor = 0.3 # Possibly temporary
friccoef = 0.5
hit_vel = 60 # Initial golf velocity in m/s

# Location
location = "Singapore" # St Andrews, Singapore or La Paz

# Air density
if location == "St Andrews":
    altitude = 0  # Altutide in m
    temperature = 14.7  # Temperature in Celcius
    wind_avg = 5  # Average wind speed in m/s
    gravity = 9.81  # in m/s^2
elif location == "La Paz":
    altitude = 3640  # Altutide in m
    temperature = 8.5  # Temperature in Celcius
    wind_avg = 4  # Average wind speed in m/s
    gravity = 9.8  # in m/s^2
elif location == "Singapore":
    altitude = 0  # Altutide in m
    temperature = 26.1  # Temperature in Celcius
    wind_avg = 3  # Average wind speed in m/s
    gravity = 9.81  # in m/s^2
#Calculation
P_0 = 101325 # Standard atmospheric pressure in Pa
R = 287.058 # Specific gas constant for air in J/kgK
air_molecule_mass = 29 # Mass of one air molecule in amu
boltzmann = 1.38e-23 # Boltzmann constant
P_h = P_0*np.e**((-(air_molecule_mass*1.66e-27)*gravity*altitude)/(boltzmann*(temperature+273.15)))
airdens = P_h/(R*(temperature + 273.15))


# Wind
random_wind = True # Set false to manually set wind values

# SET random_wind TO FALSE TO USE THESE
# THESE WILL BE OVERWRITTEN IF random_wind IS TRUE
fixed_wind_mag = 5 # Magnitude of wind in m/s
fixed_wind_angle = 10 # Angle of the wind in degrees, measured anticlockwise from the x axis


# Scene
window_x=1200 # Length of window in pixels
window_y=700 # Height of window in pixels
