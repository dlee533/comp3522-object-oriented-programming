"""
(17 marks total)
This program simulates interacting with a dog in varying states

We can interact with the dog by speaking, petting, or feeding them. The dog will
respond differently depending on the action, as well as their current state

If the dog is HAPPY, they will respond with the following interactions
speak - WOOF
pet - WOOF WOOF
feed - WOOF WOOF WOOF

If the dog is ANGRY, they will respond with the following interactions
speak - GRRR
pet - RAWR
feed - BARK

If the dog is SAD, they will respond with the following interactions
speak - ...
pet - ... ...
feed - ... ... ...

Requirements:
TODO: Implement the desired behavior above using the State design pattern. Achieve the
following output when running the program:

Dog changed to HAPPY state
speak - WOOF
pet - WOOF WOOF
feed - WOOF WOOF WOOF
Dog changed to ANGRY state
speak - GRRR
pet - RAWR
feed - BARK
Dog changed to SAD state
speak - ...
pet - ... ...
feed - ... ... ...

"""
import abc
import enum

# enums to represent the dog's mood/state
class STATE_ENUM(enum.Enum):
    HAPPY = 1
    SAD = 2
    ANGRY = 3

"""
TODO: Create a Dog class. This is the context. 
This class is capable of changing its internal state.
When the dog's state changes, all of its behaviors also change
Add methods that allow this class to
1. Change its internal state
2. Have the speak, pet, and feed behaviors
"""
class Dog:
    def __init__(self, state):
        self._state = state
        self._state.dog = self
        print("Dog changed to", self._state.state_enum.name, "state")


    def change_state(self, state):
        self._state = state
        self._state.dog = self
        print("Dog changed to", self._state.state_enum.name, "state")

    def speak(self):
        self._state.speak()

    def pet(self):
        self._state.pet()

    def feed(self):
        self._state.feed()

"""
TODO: Create an abstract State class. 
This class is the abstract class that forms the basis of all the concrete States
1. Add a dog member variable to keep track of which dog this state belongs to
2. Add a _state_enum member variable to keep track of the enum state
3. Add the abstract speak, pet, and feed behaviors
"""
class State(abc.ABC):

    def __init__(self):
        self.dog = None
        self._state_enum = None

    @property
    def state_enum(self):
        return self._state_enum

    @state_enum.setter
    def state_enum(self, state_enum):
        self._state_enum = state_enum

    @abc.abstractmethod
    def speak(self):
        pass

    @abc.abstractmethod
    def pet(self):
        pass

    @abc.abstractmethod
    def feed(self):
        pass


"""
TODO: Create a Happy State class
This class inherits from State and implements the happy speak, pet, and feed behaviors
1. Assign the _state_enum member to the appropriate enum_state
2. Add the speak, pet, and feed behaviors. Refer to the expected output to determine what
    print statements should be in each behavior
"""
class HappyState(State):

    def __init__(self):
        super()
        self.state_enum = STATE_ENUM.HAPPY

    def speak(self):
        print("speak - WOOF")

    def pet(self):
        print("pet - WOOF WOOF")

    def feed(self):
        print("feed - WOOF WOOF WOOF")



"""
TODO: Create a Sad State class
This class inherits from State and implements the sad speak, pet, and feed behaviors
1. Assign the _state_enum member to the appropriate enum_state
2. Add the speak, pet, and feed behaviors. Refer to the expected output to determine what
    print statements should be in each behavior
"""
class SadState(State):

    def __init__(self):
        super()
        self.state_enum = STATE_ENUM.SAD

    def speak(self):
        print("speak - ...")

    def pet(self):
        print("pet - ... ...")

    def feed(self):
        print("feed - ... ... ...")


"""
TODO: Create a Angry State class
This class inherits from State and implements the angry speak, pet, and feed behaviors
1. Assign the _state_enum member to the appropriate enum_state
2. Add the speak, pet, and feed behaviors. Refer to the expected output to determine what
    print statements should be in each behavior
"""
class AngryState(State):

    def __init__(self):
        super()
        self.state_enum = STATE_ENUM.ANGRY

    def speak(self):
        print("speak - GRRR")

    def pet(self):
        print("pet - RAWR")

    def feed(self):
        print("feed - BARK")


# DON'T TOUCH CODE BELOW
# helper function to interact with dog
def interact_with_dog(dog):
    dog.speak()
    dog.pet()
    dog.feed()

def main():

    happy_state = HappyState()
    angry_state = AngryState()
    sad_state = SadState()

    dog = Dog(happy_state)
    interact_with_dog(dog)
    """
    Expected output: 
    Dog changed to HAPPY state
    speak - WOOF
    pet - WOOF WOOF
    feed - WOOF WOOF WOOF
    """

    dog.change_state(angry_state)
    interact_with_dog(dog)
    """
    Expected output: 
    Dog changed to ANGRY state
    speak - GRRR
    pet - RAWR
    feed - BARK
    """

    dog.change_state(sad_state)
    interact_with_dog(dog)
    """
    Expected output: 
    Dog changed to SAD state
    speak - ...
    pet - ... ...
    feed - ... ... ...
    """
# DON'T TOUCH CODE ABOVE

if __name__ == '__main__':
    main()