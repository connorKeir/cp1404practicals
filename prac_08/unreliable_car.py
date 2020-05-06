"""
CP1404 Practical
Car class - Unreliable Class
"""
from prac_08.car import Car
from random import randrange


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if randrange(0, 101) <= self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = super().drive(0)
        return distance_driven
