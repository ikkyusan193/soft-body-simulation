# Vector.py 
# a Vector class, this is a object class representing a Vector (2D),
# This class will contain function of standard arithmetic operations between vectors and coefficients
# We will achieve this by using help from NumPy Library
#
# idea from: Princeton CS
# https://introcs.cs.princeton.edu/python/33design/vector.py.html


#imports
import numpy as np
import math

class Vector:

    x = 0
    y = 0

    # Construct a new 2D Vector Object
    # The defualt for x and y is set at 0 if no input are given
    # @param        x: position at x-axis (horizontal)
    # @param        y: position at y-axis (vertical)
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        

    # Calculate the magnitude/lenght of the given vector
    # @param        self: current vector
    # @return       Return the magnitude/vector of the vector
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
    length =  __abs__

    # Generate a zero vector
    # @return       Return new Vector(0,0)
    def zero(self):
        return Vector(0.0,0.0)   


    # Calculate the distance between two vector
    # @param        self: vector1
    # @param        other: vector2
    # @return       Return the distance between two vector
    def __distance__(self,other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


    # Calculate the dot product between two vector
    # @param        self: vector1
    # @param        other: vector2
    # @return       Return a number of the dot product between vector1 and vector2
    def __dot__(self, other):
        return (self.x * other.x) + (self.y * other.y)


    # Vector addition & Vector subtraction
    # @param        self: vector1
    # @param        other: vector2
    # return        Return new vector object after the arithmetical operations
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)   

    def __mul__(self, k):
        self.x *= k
        self.y *= k
        return Vector(self.x,self.y)

    def __rev__(self):
        self.x = -self.x
        self.y = -self.y
        return Vector(self.x, self.y)     


    # Multiply a vector with another vector
    # @param        self: vector1
    # @param        other: vector2
    # @return       Return a vector after its multiplcation with another vector
    def scale(self, other):
        self.x *= other.x
        self.y *= other.y
        return self


    # Check if both given vector are equals
    # @param        self: vector1    
    # @param        other: vector2     
    # @return       Return true if vector1 and vector2 is equal
    #               (They have the same x,y)
    def __iseq__(self,other):
        return self.x == other.x and self.y == other.y


    # @TODO fix this by using numpy
    # Normalize a given vector 
    # @param        self: current vector   
    def normalize(self):
        l = self.length()
        if l:
            self.x = self.x / l
            self.y = self.y / l
        return self     


    # @TODO fix this by using numpy
    # Normalize a given vector and returning a new one
    # @param        self: current vector
    # @return       Return a "normalized" vector
    def normalized(self):
        l = self.length()
        if l:
            return Vector(self.x / l, self.y / l)





