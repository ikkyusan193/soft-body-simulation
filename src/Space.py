# Space.py
# This is a custom-built simulation space where:
# we can customize our simulation constant such as gravity, damping factor and etc.
# This simulation space will contain a list of particles with its constraint
# This is where we combine all the neccesary class to build a simulation as a whole.

class Space:


    # Variables with explanation
    #
    # @var      gravity: simulation's gravitational acceleration
    # @var      height: simulation's space height
    # @var      width: simulation' space width
    # @var      step: simulation step
    # @var      delta: amount of time between step in the simulation
    # @var      particles[]: list of particles for the simulation
    # @var      constraints[]: list of constraints for the simulation
    # @var      shapes[]: list of shapes for the simulation
            
    # Constants
    gravity = 0
    height = 0
    width = 0
    # Simulation setting
    step = 0 
    delta = 0
    # List of neccesary components
    particles = []
    constraints = []
    shapes = []

    def __init__(self):
        #TODO
        return

    