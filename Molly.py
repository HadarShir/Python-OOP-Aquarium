from Fish import Fish
from Exceptions import *


class Molly(Fish):
    # This class represents a specific species of fish that belongs to the Fish class and, in turn, belongs to the Animal class.
    # Therefore, it inherits the properties accordingly.
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, 8, 3, directionH, directionV, 'molly')
        # It inherits the constructor from the Fish class.

    def get_animal(self): # The unique shape of the fish.
        if self.directionH == 0:  # molly_left
            return [[" ", "*", "*", "*", "*", " ", " ", "*"],
                    ["*", "*", "*", "*", "*", "*", "*", "*"],
                    [" ", "*", "*", "*", "*", " ", " ", "*"]]
        if self.directionH == 1:  # moly_right
            return [["*", " ", " ", "*", "*", "*", "*", " "],
                    ["*", "*", "*", "*", "*", "*", "*", "*"],
                    ["*", " ", " ", "*", "*", "*", "*", " "]]
