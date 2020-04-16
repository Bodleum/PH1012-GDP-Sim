import random

# Universal
gravity = 9.81 # in m/s^2


# Visual
radius_scale = 150 # Multiplier to artificially inflate the golf ball's size, bigger means larger ball
                   # VISUAL ONLY
distance_scale = 4.5 # Multiplier for how zoomed in/out the scene is, bigger means more zoomed in
ground_height = 620 # How high the ground is in pixels, reccomend not changing
flag_spacing = 50 # Distance between flags in m
flag_range = 400 # Furthest out flag marker in m


# Golf ball
golf_ball_mass = 0.05 # Mass of golf ball in kg
golf_ball_radius = 0.02 # Radius of golfball in m
dragcoef = 0.35 # Drag coefficient of golf ball, larger means more air resistance, 0 is no air resistance


# Location
airdens = 1.2041  # from Wikipedia -> temporary
wind_avg = 5 # Average wind speed in m/s


# Scene
window_x=1200 # Length of window in pixels
window_y=700 # Height of window in pixels