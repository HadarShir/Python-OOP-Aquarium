from Crab import Crab
from Exceptions import *


class Ocypode(Crab):
    # This class represents a specific species of crab that belongs to the Crab class and, in turn, belongs to the Animal class.
    # Therefore, it inherits the properties accordingly.
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y,7, 4, directionH,'ocypode')
        # It inherits the constructor from the Fish class.

    def get_animal(self):  # The unique shape of the carb.
        return [[" ", "*", " ", " ", " ", "*", " "],
                [" ", " ", "*", "*", "*", " ", " "],
                ["*", "*", "*", "*", "*", "*", "*"],
                ["*", " ", " ", " ", " ", " ", "*"]]
