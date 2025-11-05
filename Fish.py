from Animal import Animal
from Exceptions import *


class Fish(Animal):
    # A class that inherits from the Animal class, representing common properties for fish. Subsequently,
    # specific types of fish will inherit from it.
    def __init__(self, name, age, x, y, width, height, directionH, directionV, typeanimal):
        # Class constructor, we added a property specific to fish, the ability to move up and down.
        super().__init__(name, age, x, y, width, height, directionH, typeanimal)
        # It inherits the constructor from the Animal class.
        if not isinstance(directionV, int) or directionV not in [0, 1]:
            raise InvalidInputException("directionV must be 0 or 1.")

        self.directionV = directionV
        self.width = 8

    def get_directionV(self):
        return self.directionV

    def move(self):  # Definition of the movement ability and the impact of the values.
        if self.directionV == 0:
            self.y = self.y + 1
        if self.directionV == 1:
            self.y = self.y - 1
        if self.directionH == 0:
            self.x = self.x - 1
        if self.directionH == 1:
            self.x = self.x + 1

    def set_directionV(self, directionV):
        self.directionV = directionV


