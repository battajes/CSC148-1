# Exercise 2: Cars and Hover Cars
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your information below, in format
# <Singh Naina>, <1000689098>
#
# ---------------------------------------------
import math


class NotEnoughFuelError(Exception):
    pass


class Car:

    # Don't change this code!
    def __init__(self, fuel, efficiency):
        """ (Car, int, int) -> NoneType

        fuel is an int specifying the starting amount of fuel. 
        efficiency is an int specifying how much fuel the car takes
        to travel 1 unit of distance.

        Initialize a new car with an amount of fuel and a fuel efficiency.
        The car's starting position is (0,0).
        """

        self.fuel = fuel
        self.efficiency = efficiency
        self.pos_x = 0
        self.pos_y = 0

    def move(self, new_x, new_y):
        """ (Car, int, int) -> NoneType

        Move the car from its old position to (new_x, new_y).
        Reduce the car's fuel depending on its efficiency and how far it
        travelled.

        If there isn't enough fuel to reach (new_x, new_y),
        do not change car's position or fuel level.
        Instead, raise NotEnoughFuelError.

        Remember that the car can only travel horizontally and vertically!
        """
        
        distance_to_travel = math.fabs(new_x) + math.fabs(new_y)

        
        if (distance_to_travel) > self.fuel/self.efficiency : 
            raise NotEnoughFuelError  
        
        if distance_to_travel==0 and self.fuel==0: 
            self.pos_x = new_x
            self.pos_y = new_y
            self.fuel = self.fuel
    
        else: 
            self.pos_x = new_x
            self.pos_y = new_y
            self.fuel = int((self.fuel/self.efficiency) - (distance_to_travel))
            
        pass 
        


class HoverCar(Car):

    def __init__(self, fuel, efficiency, hover_fuel):
        """ (HoverCar, int, int, int) -> NoneType

        hover_fuel is an int specifying the starting amount of hover fuel.

        Initialize a new HoverCar
        
        20 units of distance for 1 fuel.
        hover fuel allows it to travel diagonally, normal fuel vertically 
        and horizontal
        only uses hover fuel if not enough normal
        """
        Car.__init__(self, fuel, efficiency)
        self.hover_fuel = hover_fuel

    def move(self, new_x, new_y):
        """ (HoverCar, int, int)

        Move the hover car according to the description in the exercise.
        Remember that hover cars try using regular fuel first,
        and only use hover fuel if there isn't enough regular fuel.

        Be sure to follow the implementation guidelines for full marks!
        """
        
        distance_to_travel =  math.sqrt((new_x**2) + new_y**2)
        
        try: 
            Car.move(self, new_x, new_y)
                
        except NotEnoughFuelError:
            if (self.hover_fuel * 20) >= distance_to_travel:
                self.hover_fuel = math.floor(self.hover_fuel - (distance_to_travel/20))
                self.pos_x = new_x
                self.pos_y = new_y                
                
            elif (self.hover_fuel * 20) < distance_to_travel:  
                raise NotEnoughFuelError
        pass 
                