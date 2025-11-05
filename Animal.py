from abc import ABC, abstractmethod
from Exceptions import *


class Animal(ABC):
    #This class is the parent class defining what an animal is. Subclasses inherit basic properties that are common to all.
    def __init__(self, name, age, x, y, width, height, directionH, typeanimal):
        #The class constructor defines properties that are common to all animals.
        if not isinstance(name, str):
            raise InvalidInputException("Name must be a string.")
        elif len(name) == 0:
            raise InvalidInputException("Name must be a non-empty string.")

        if not isinstance(age, int):
            raise InvalidInputException
        elif age < 0 or age >= 120:
            raise InvalidInputException("Age must be a number between 0 and 120.")

        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise InvalidInputException("x and y must be non-negative number.")

        if not isinstance(directionH, int) or directionH not in [0, 1]:
            raise InvalidInputException("directionH must be 0 or 1.")

        self.age = age
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.directionH = directionH
        self.food = 10
        self.typeanimal = typeanimal

    def __str__(self):  #Common string that will be printed for all animals.
        return f'The {self.typeanimal} {self.name} is {self.age} years old and has {self.food} food.'

    @abstractmethod
    def get_animal(self): #A class that exists for all animals but is separately defined in each subclass.
        pass

    def __repr__(self):  #A function that generates the printing output for the animal.
        animal = self.get_animal()
        output_animal = ''
        for row in animal:
            for i in row:
                output_animal += i + ' '
            output_animal = output_animal[0:-1] + '\n'
        return output_animal

    def get_position(self):
        return self.x, self.y

    def get_directionH(self):
        return self.directionH

    def get_size(self):
        return self.width, self.height

    def dec_food(self):
        self.food = self.food - 1

    def add_food(self, amount):
        self.food = self.food + amount

    def inc_age(self):
        self.age = self.age + 1

    @abstractmethod
    def move(self):
        #Since not all animals move in the same way but all have the ability to move, we will define it here and then
        # override it in each class.
        pass

    def set_directionH(self, directionH):
        self.directionH = directionH

    def starvation(self): #Common string that will be printed for all animals.
        if self.food == 0:
            print(f' {self.name} died at the age of {self.age} years because it ran out of food.')
            return True
        else:
            return False

    def die(self): #Common string that will be printed for all animals.
        if self.age >= 120:
            print(f' {self.name} died in a good health.')
            return True
        else:
            return False
