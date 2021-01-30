"""
This module creates a list of asteroid objects and drives the program, simulating asteroids
moving within a specific amount of time.
Dongmin(Mina) Lee, Michelle Huynh
"""

import random
import datetime
import math
import time

from Lab.Lab2.asteroid import Asteroid  # change the package name before running on your machine
from Lab.Lab2.asteroid import Vector  # change the package name before running on your machine


class Controller:
    """This Controller class is used to simulate the Asteroid class."""

    def __init__(self) -> None:
        """
        Initialize the Controller object.
        """
        self._asteroids = []

        num_asteroid = 100
        radius_min = 1
        radius_max = 4
        position_min = 0
        position_max = 100
        velocity_min = 0
        velocity_max = 5

        for i in range(num_asteroid):
            radius = random.randint(radius_min, radius_max)
            circumference = 2 * math.pi * radius
            position = Vector(random.randint(position_min, position_max), random.randint(position_min, position_max),
                              random.randint(position_min, position_max))
            velocity = Vector(random.randint(velocity_min, velocity_max), random.randint(velocity_min, velocity_max),
                              random.randint(velocity_min, velocity_max))
            asteroid = Asteroid(circumference, position, velocity)
            self._asteroids.append(asteroid)

    def simulate(self, seconds: int) -> None:
        """
        Run the simulation.
        :param seconds: int
        :precondition: seconds must be an int
        :return: none
        """
        if datetime.datetime.now().microsecond != 0:
            time.sleep(1 - (datetime.datetime.now().microsecond * math.pow(10, -6)))

        print(f"Simulation Start Time: {datetime.datetime.now()}\n\n")
        print("Moving Asteroids!")
        print("-----------------")

        for second in range(seconds):
            for asteroid in self._asteroids:
                asteroid.move()
                print(asteroid)
            time.sleep(1)
            print()


def main() -> None:
    """
    Instantiate a Controller and the simulation.
    :return: none
    """
    seconds = 5
    controller = Controller()
    controller.simulate(seconds)


if __name__ == "__main__":
    main()
