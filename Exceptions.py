class InvalidInputException(Exception):
    """Raised when an invalid input is provided."""
    pass


class NotAvailablePlace(Exception):
    """Raised when attempting to place an animal in an occupied spot."""
    pass


class TooSmallAquariumSize(Exception):
    """Raised when the requested size for an aquarium is smaller than the allowable limit."""
    pass


class InvalidAnimalType(Exception):
    """Raised when trying to add an animal to the aquarium of a type that does not exist."""

    def __init__(self, animaltype):
        self.animaltype = animaltype

    def __str__(self):
        return f'Error: \"{self.animaltype}\" is an invalid animal type. Valid animal types are: molly, scalar, ocypode, shrimp.'