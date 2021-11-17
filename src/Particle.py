from Properties import *
from Vector import *

class Particle:
    
    properties = None # Properties is where the constant reside
    position = Vector(0.0,0.0) # Current position of the vector
    previous = Vector(0.0,0.0) # Previous position of the vector, position relative to the last time step
    velocity = Vector(0.0,0.0) # Velocity: the rate of change of position with respect to time
    acceleration = Vector(0.0,0.0) # Acceleration: the rate of change of velocity


    # Particle Class: Initializing the particle with its properties
    # [Constructor]
    # @param    x: Particle horizontal position, default is set at x = 0
    # @param    y: Particle vertical position, default is set at y = 0
    # @param    properties: Properties of the particle including gravity, mass and etc.
    def __init__(self, x=0.0, y=0.0, properties=None):

        if properties == None:
            self.material = Properties()
        else:
            self.material = properties
        self.position = Vector(x,y)
        self.previous = Vector(x,y)


