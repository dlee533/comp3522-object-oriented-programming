"""
12 Marks

You are running a car body shop that adds different modifications to cars.

For this question, you will be simulating the effects adding these different modifications
 will have on a car.

All modifications will affect the following properties of the car:
- aesthetics
- speed

These two attributes together create the car profile.

Your task for this question is to implement the decorator pattern and
implement three decorator classes, each represents one of the
following modifications given below. Each decorator will return a modified
car profile. The modifications (decorators) you will implement are:

Spoiler:
 - aesthetics: +50
 - speed: + 100

Neon lights:
  - aesthetics: +200
  - speed: +50

Tire rims:
  - aesthetics: + 100
  - speed: - 300

Requirements:
The Car class has been written and provided for you. You must
write all the code necessary to decorate the car with all three
modifications. Add code as indicated by the TODO comments.
Complete this program with a main method that creates a car and
decorates it with all three modifications.

"""
import abc


class Car:
    """
    This class represents the concrete Car whose profile is being
    simulated.
    """

    def __init__(self, aesthetics: int = 10, speed: int = 10):
        """
        Initialize a car with its profile.
        :param aesthetics: an int
        :param speed: an int
        """
        self._aesthetics = aesthetics
        self._speed = speed

    @property
    def aesthetics(self) -> int:
        """
        READ ONLY property to access the aesthetics value.
        :return: an int
        """
        return self._aesthetics

    @property
    def speed(self) -> int:
        """
        READ ONLY property to access the speed value.
        :return: an int
        """
        return self._speed

    def process_profile(self) -> dict:
        """
        Process and return the profile as a dictionary.
        :return: a dictionary (string: int)
        """
        profile = {
            "Aesthetics": self.aesthetics,
            "Speed": self.speed
        }
        return profile


class BaseCarDecorator:
    #TODO: Implement the BaseCarDecorator
    def __init__(self, car):
        self.car = car
        self.profile = car.process_profile()


class SpoilerDecorator(BaseCarDecorator):
    #TODO: Implement the SpoilerDecorator
    def process_profile(self):
        self.profile["Aesthetics"] +=50
        self.profile["Speed"] += 100
        return self.profile


class NeonLightsDecorator(BaseCarDecorator):
    #TODO: Implement the NeonLightsDecorator
    def process_profile(self):
        self.profile["Aesthetics"] += 200
        self.profile["Speed"] += 50
        return self.profile



class TireRimsDecorator(BaseCarDecorator):
    #TODO: Implement the TireRimsDecorator
    def process_profile(self):
        self.profile["Aesthetics"] += 100
        self.profile["Speed"] -= 300

        return self.profile



def main():
    car = Car(200, 200) #Don't modify this line

    # TODO: Decorate car with spoiler, neon lights and tire rims
    #  decorators.
    car = SpoilerDecorator(car)
    car = NeonLightsDecorator(car)
    car = TireRimsDecorator(car)

    # Don't modify code below
    profile = car.process_profile()

    # Expected Output after decoration:
    # Aesthetics: 500
    # Speed 550
    for key, val in profile.items():
        print(f"{key}: {val}")


if __name__ == '__main__':
    main()