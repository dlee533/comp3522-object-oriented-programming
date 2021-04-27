import threading
import time
import logging

"""
(5 marks total)
This program simulates 4 car manufacturers that take some time to make cars
The code below takes around 2 seconds (on my machine) to run. 

Requirements:
4 car manufacturers must exist (ie: not allowed to only have 1 car manufacturer)
CarManufacturer class must exist
Rewrite the code using MULTITHREADING to speed up the execution time.
CarManufacturer class inherits from the Thread class.

Do NOT use the threadpool executor

Hint: 
It should take around 1/4 of the time (0.5 seconds on my machine) after optimizations
"""


class CarManufacturer(threading.Thread):
    id = 0

    @classmethod
    def increment_id(cls):
        cls.id += 1
        return cls.id

    def __init__(self):
        super().__init__()
        self.id = self.increment_id()

    def make_car(self):
        logging.info(f"CarManufacturer {self.id} making car")
        time.sleep(0.5)
        logging.info(f"CarManufacturer {self.id} finished car")

    def run(self):
        self.make_car()

def main():
    start_time = time.time()

    threads = [CarManufacturer() for _ in range(4)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    duration = time.time() - start_time
    logging.info(f"Made cars in {duration} seconds")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    main()