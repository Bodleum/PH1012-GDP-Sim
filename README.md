# PH1012-GDP-Sim

### Golf simulation for the GDP in PH1012.  

NOTE!! THE MODEL REQUIRES THE NUMPY MODLUE!!

The file to run is "GDP_Sim.py".

Variables like the drag coefficient, gravity, etc. can be changed in "data/constants.py"

The output is in "logs" folder.

### Explanation:

The basic idea of the model is to have a loop that increments time and then moves the golf ball accordingly.
The smaller the time step each time, the more precice the model is but the slower and more computationally expensive it is.
We used increments of 0.0075 seconds as a good middle ground.

"data/constants.py" contains many values affecting the model which can be easily changed.

I started by definig a vector class in "Vector.py" to help easily manipulate vectors.
It stores the x and y components, the total magnitude and the angle of the vector and also contains some basic functions for adding two vectors.
I then defined a ball class in "Ball.py" to represent the golf ball.
It sotres some basic information about the golfball such as mass, radius, ect as well as a list of velocities and accelerations acting on it.
The ball class also contains some more complex functions to calculate bouncing and rolling however the update() function does all the hard work.
This is the function that determines how the bal moves.

Ball.update() takes in the time step (tstep) and also the current wind.
It first sums all accelerations acting on the ball into one vector then calculates the velocity step for the current increment.
It then does the same for velocity, including the increment caused by the acceleration.
The distance increase in both the x and y directions are calculated and then added to the curent x and y positions.
The relative velocity to the wind is calculated and then the acceleration list cleared. This is done to stop cumulative acceleration.
If the ball is in the air, then gravity, air resistance and spin lift force are all calcuated and added to the now blank acceleration list.
It the ball is on the ground then the roll friction is applied.
Ball.bounce() simply flips the y component of the velocity and decreases it by a factor of the coefficient of restitution.
Ball.roll() removes all velocities and adds a small x component. 

"GDP_Sim.py" is where all these functions are called from and contains the loop which iterates the Ball.update() function.
It starts by defining a few variables and then opens an output file.
The wind is determined and then asks the user if they would like to draw the simulation and sweep through multiple angles in turn.
The main simulate() function is defined. In it we first create the golf ball using the Ball class and add the initial velocity to it.
Then we create some visual objects like the ground, clouds and so on if the user wanted to draw.
We create a window and then draw the ojbects to it.
Then the main_loop() function is defined. This is the heart of the model. 
While the model is active (indicated by the "model" boolean) we call Ball.update(), then test to see if it's above the ground. If it isn't then we call Ball.bounce().
If the bounce velocity is too low then we instead call Ball.roll().
We check if the ball is close enough to the edge of the screen to scroll and if it is the keep the ball where is it and instead move everyting else backwards. 
Various components in the display window are updated and this loops until the ball has stopped.
We then print the results and write them to a file. This ends main_loop().
Finally we call main_loop() at the end of simulate().

One last function, dosweep() is defined which just repeatedly calls simulate() with incrementing angles and saves the results.

The if the user opted not to sweep angles then we ask for an inital velocity magnitude and angle then runs simulate() once and prints the results.

Else, we repeatedly call dosweep() which in turn repeatedly calls simulate().
The number of times we call dosweep() is determined by the "while q < 20" test, so dy default we repeat 20 times.
Finally the program prints the top three results and then closes the output files.