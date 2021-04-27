"""
(36 Marks total)
In this module we will write code to simulate cars responding to a traffic light using the Observer Design Pattern.
In this program, the traffic light acts as the core, with the cars acting as observers
Cars will respond to the traffic light as it changes colors

The system will be written over several steps marked by the comments below.
Import any libraries and add any additional methods you need to achieve the tasks
Write your code below each of the steps
"""
import abc
from enum import Enum, auto

"""
(3 marks) 
Create a TrafficLightStatus enum that contains four enum members: RED, YELLOW, GREEN, INVALID
"""


class TrafficLightStatus(Enum):
    RED = auto()
    YELLOW = auto()
    GREEN = auto()
    INVALID = auto()


"""
(3 marks)
Create a custom exception named InvalidLightException. This exception will be raised if a 
Car needs to respond to an INVALID TrafficLightStatus. 

When this exception is printed, it will display a custom message: 
"Error Invalid light:" appended with the name of the TrafficLightStatus that caused
the error. 
ie: "Error Invalid light: INVALID" is printed if an INVALID TrafficLightStatus was raised

    •	Create a custom exception, InvalidLightException, that inherits from Exception
    •	The initializer accepts a TrafficLightStatus enum parameter.
    •	Write code in the initializer to support the custom exception message
"""


class InvalidLightException(Exception):

    def __init__(self, traffic_light_status):
        self._traffic_light_status = traffic_light_status
        message = "Error Invalid light: " + TrafficLightStatus(traffic_light_status).name
        super().__init__(message)


"""
(4 marks) 
Create an abstract Observer class
    •	Create an abstract method named update that accepts traffic_light as a parameter
        o	The body of the abstract method is empty
"""


class Observer(abc.ABC):

    @abc.abstractmethod
    def update(self, traffic_light):
        pass


"""
(7 marks) 
Create a Car class that inherits from Observer. 
This class listens to changes when TrafficLight calls its update method. This class contains:
•	update method – prints a different message depending on the traffic light parameter that’s passed in
    o	Accepts a traffic_light parameter of enum type TrafficLightStatus
    o	Prints “Stop” on red light 
    o	Prints “Slow down” on yellow light 
    o	Prints “Go” on green light 
    o	Raises an InvalidLightException on invalid light
        - pass traffic_light as argument to InvalidLightException
"""


class Car(Observer):

    def update(self, traffic_light):
        if traffic_light == TrafficLightStatus.RED:
            print("Stop")
        elif traffic_light == TrafficLightStatus.YELLOW:
            print("Slow down")
        elif traffic_light == TrafficLightStatus.GREEN:
            print("Go")
        else:
            raise InvalidLightException(traffic_light)


"""
(11 marks) 
TODO Create a TrafficLight class. 
This class behaves as the core, which broadcasts information out to observers. 
This class contains:
    •	initializer method – Initializes the TrafficLight class
        o	_light is a TrafficLightStatus enum set to INVALID by default
        o	_observers is a list of observers initialized to an empty list
    •	attach method – Adds new observers to the list of observers
        o	Accepts one parameter observer of type Observer
        o	Adds the observer parameter to the _observers list
    •	detach method – Removes an observer from the list of observers
        o	Accept one parameter observer of type Observer
        o	Removes the observer from the _observers list
    •	notify method – Accepts a light enum and notifies all observers of the new light enum
        o	Accepts a parameter of type TrafficLightStatus
        o	Sets _light to the new value
        o	Calls all observers and informs them of the new _light
"""


class TrafficLight:

    def __init__(self):
        self._light = TrafficLightStatus.INVALID
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, light):
        self._light = light
        for observer in self._observers:
            observer.update(self._light)


"""
(5 marks)
TODO Write some code to test out the observer pattern.
•	Create three Car objects
•	Create one TrafficLight object
•	Attach all three cars to the TrafficLight object
•	Notify the light has changed to YELLOW using the TrafficLight object
•	Detach one of the cars from the TrafficLight object
•	Notify the light has changed to GREEN using the TrafficLight object
•	Notify the light has changed to INVALID using the TrafficLight object
•	Handle InvalidLightException with try except blocks and print out exception message
"""

car1 = Car()
car2 = Car()
car3 = Car()

trafficLight = TrafficLight()

trafficLight.attach(car1)
trafficLight.attach(car2)
trafficLight.attach(car3)

trafficLight.notify(TrafficLightStatus.YELLOW)

trafficLight.detach(car1)

trafficLight.notify(TrafficLightStatus.GREEN)

try:
    trafficLight.notify(TrafficLightStatus.INVALID)
except InvalidLightException as e:
    print(e)


"""
(3 marks)
TODO Write the output when running the program in the area below:

Slow down
Slow down
Slow down
Go
Go
Error Invalid light: INVALID

"""
