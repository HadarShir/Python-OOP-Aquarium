from Crab import Crab
from Exceptions import *


class Shrimp(Crab):
    def __init__(self, name, age, x, y, directionH):
        # This class represents a specific species of crab that belongs to the Crab class and, in turn, belongs to the Animal class.
        # Therefore, it inherits the properties accordingly.
        super().__init__(name, age, x, y, 7, 3, directionH,'shrimp')
        # It inherits the constructor from the Fish class.

    def get_animal(self):  # The unique shape of the carb.
        if self.directionH == 0:  # shrimp_left
            return [["*", " ", "*", " ", " ", " ", " "],
                    [" ", "*", "*", "*", "*", "*", "*"],
                    [" ", " ", "*", " ", "*", " ", " "]]
        if self.directionH == 1:  # shrimp_right
            return [[" ", " ", " ", " ", "*", " ", "*"],
                    ["*", "*", "*", "*", "*", "*", " "],
                    [" ", " ", "*", " ", "*", " ", " "]]