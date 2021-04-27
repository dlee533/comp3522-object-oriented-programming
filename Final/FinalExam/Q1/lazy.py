import time

"""
(4 marks total)
This program simulates loading screens in a game. One of the screens is entered and resources
need to be loaded, the other does not
The code below takes about 1 second (on my machine) to complete.

Requirements
Speed up the code using the LAZY INITIALIZATION design pattern.
Do NOT change any code in the main function

Hints: 
The code should run in about half the time after implementing Lazy Initialization
There is no need to use any multithreading/multiprocessing
"""

class Resources:
    def __init__(self):
        print("Creating resources")
        time.sleep(0.5)

    def __str__(self):
        return "resources available"

class Screen:

    def __init__(self, name):
        self._name = name
        self._resources = None

    def enter_screen(self):
        if not self._resources:
            self._resources = Resources()
        return self._resources

    def __str__(self):
        return self._name

def main():
    start_time = time.time()
    game_over = Screen("Game over")
    print(game_over)

    main_menu = Screen("Main menu")
    print(main_menu)
    print(main_menu.enter_screen())
    end_time = time.time()
    print("duration:", end_time - start_time)

if __name__ == '__main__':
    main()