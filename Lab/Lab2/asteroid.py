"""
This module represents asteroids and vectors and its basic attributes and behaviours.
Dongmin(Mina) Lee, Michelle Huynh
"""


class Vector:
    """A data type to store x, y, z coordinates."""

    def __init__(self, x: int, y: int, z: int) -> None:
        """
        Initialize the x, y, z dimensions of a vector.
        :param x: an int
        :param y: an int
        :param z: an int
        :precondition: x must be an int
        :precondition: y must be an int
        :precondition: z must be an int
        """
        self._x = x
        self._y = y
        self._z = z

    def get_x(self) -> int:
        """
        Return x coordinate.
        :return: x coordinate
        """
        return self._x

    def get_y(self) -> int:
        """
        Return y coordinate.
        :return: y coordinate
        """
        return self._y

    def get_z(self) -> int:
        """
        Return z coordinate.
        :return: z coordinate
        """
        return self._z

    def set_x(self, x: int) -> None:
        """
        Change value of x.
        :param x: int
        :precondition: x must be an int
        :return: none
        """
        self._x = x

    def set_y(self, y: int) -> None:
        """
        Change value of y.
        :param y: int
        :precondition: y must be an int
        :return: none
        """
        self._y = y

    def set_z(self, z: int) -> None:
        """
        Change value of z.
        :param z: int
        :precondition: z must be an int
        :return: none
        """
        self._z = z

    def get_vector_as_tuple(self) -> tuple:
        """
        Return coordinates as a tuple.
        :return: x, y, z coordinates of vector as a tuple
        """
        return self._x, self._y, self._z

    def add(self, vector) -> None:
        """
        Add coordinates of one vector to the coordinates of self.
        :param vector: a Vector object
        :precondition: vector must be an object of Vector class
        :return: none
        """
        self._x = self._x + vector.x
        self._y = self._y + vector.y
        self._z = self._z + vector.z

    def __repr__(self) -> str:
        """
        Return unambiguous string describing state of object
        :return: string
        """
        return f"x = {self.x}, y = {self.y}, z = {self.z}"

    def __str__(self) -> str:
        """
        Return string with values of attributes of the object.
        :return: string with attribute values
        """
        return f"{self._x}, {self._y}, {self._z}"

    x = property(get_x, set_x)
    y = property(get_y, set_y)
    z = property(get_z, set_z)


class Asteroid:
    """A class used to represent an asteroid."""
    unique_id = 1

    def __init__(self, circumference: float, position: Vector, velocity: Vector) -> None:
        """
        Initialize attributes to describe an asteroid.
        :param circumference: float
        :param position: Vector
        :param velocity: Vector
        :precondition: circumference must be a float
        :precondition: position must be a Vector with x,y,z coordinates
        :precondition: velocity must be a Vector with x,y,z coordinates
        """
        self._circumference = circumference
        self._position = position
        self._velocity = velocity
        self._id = Asteroid.unique_id
        Asteroid.increment_id()

    def get_circumference(self) -> float:
        """
        Return the circumference of asteroid.
        :return: float
        """
        return self._circumference

    def get_position(self) -> Vector:
        """
        Return the position of asteroid.
        :return: Vector with x,y,z coordinates
        """
        return self._position

    def get_velocity(self) -> Vector:
        """
        Return the velocity of asteroid.
        :return: Vector with x,y,z values
        """
        return self._velocity

    def get_id(self) -> int:
        """
        Return the asteroid id.
        :return: int
        """
        return self._id

    def move(self) -> None:
        """
        Change the position of asteroid.
        :return: none
        """
        old_position = self.get_position().get_vector_as_tuple()
        self.get_position().add(self.get_velocity())
        print(f"Asteroid {self.get_id()} Moved! Old pos: {old_position[0]}, {old_position[1]}, {old_position[2]} "
              f"-> New Pos: {self.get_position()}")

    @classmethod
    def increment_id(cls):
        """
        Increment id.
        :return: none
        """
        cls.unique_id += 1

    def __repr__(self) -> str:
        """
        Return unambiguous string describing state of object
        :return: string
        """
        return f"id = {self.get_id()}, circumference = {self.get_circumference()}, position = {self.get_position()}, " \
               f"velocity = {self.get_velocity()} "

    def __str__(self) -> str:
        """
        Return a formatted string.
        :return: string describing the state of the asteroid
        """
        return f"Asteroid {self.get_id()} is currently at {self.get_position()} and moving at {self.get_velocity()} " \
               f"metres per second. It has a circumference of {self.get_circumference()}"
