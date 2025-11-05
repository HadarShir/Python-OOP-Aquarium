from Animal import Animal
from Exceptions import *


class Crab(Animal):
    # A class that inherits from the Animal class, representing common properties for Crabs.
    # Subsequently, specific types of crabs will inherit from it.
    def __init__(self, name, age, x, y, width, height, directionH, typeanimal):
        super().__init__(name, age, x, y, width, height, directionH,typeanimal)
        # It inherits the constructor from the Animal class.

    def move(self):  ## Definition of the movement ability and the impact of the values.
        if self.directionH == 0:
            self.x = self.x - 1
        if self.directionH == 1:
            self.x = self.x + 1
