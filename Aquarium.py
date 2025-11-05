from Animal import Animal
from Exceptions import *
from Crab import Crab
from Molly import Molly
from Scalar import Scalar
from Ocypode import Ocypode
from Shrimp import Shrimp
from Fish import Fish


class Aquarium:
    def __init__(self, aqua_width, aqua_height):  #Aquarium class constructor.
        self.step = 0
        self.animals = []
        if not isinstance(aqua_height, int):  #User input validation.
            raise InvalidInputException('Height is not integer')
        if not isinstance(aqua_width, int):  #User input validation.
            raise InvalidInputException('Width is not integer')
        if aqua_height < 25:  #User input validation.
            raise TooSmallAquariumSize("Too Small Aquarium Size.")
        if aqua_width < 40:  #User input validation.
            raise TooSmallAquariumSize("Too Small Aquarium Size.")

        self.aqua_width = aqua_width
        self.aqua_height = aqua_height

        # Aquarium creation process.
        bottom_line = []
        water_line = []
        board = []
        for i in range(aqua_height):
            row = [' '] * aqua_width
            board.append(row)
        for i in range(aqua_width):
            water_line.append('~')
            bottom_line.append('_')

        board[2] = water_line
        board[-1] = bottom_line
        index = [0,-1] ן
        for line in range(len(board)):
            for i in index:
                board[line][i] = '|'
        board[-1][0], board[-1][-1] = '\\', '/'

        self.board = board

    def __str__(self):
        string = f'The aquarium, sized {self.aqua_height}/{self.aqua_width} and currently in step {self.step}, contains the following animals:\n'
        for animal in self.animals:
            string += str(animal) + '\n'
        return string

    def __repr__(self):  # Representation the print of the class .
        s = ''
        for list in self.board:
            for i in list:
                s = s + i + ' '
            s = s[:-1] + '\n'
        return s

    def feed_all(self):
        for animal in self.animals:
            animal.add_food(10)

    def __insert_animal_to_board(self, animal):  # Private Method
        animal_shape = animal.get_animal()
        x, y = animal.get_position()  # Representation of the coordinates at which the animal is located.
        width, height = animal.get_size()

        for line in range(y, y+height):  # Represents the number of rows occupied by the animal.
            for place in range(x, x+width): # Represents the number of columns occupied by the animal.
                if animal_shape[line - y][place - x] == '*': # Iterates over the list and inserts only '*'
                    self.board[line][place] = animal_shape[line - y][place - x]

    def __delete_animal_from_board(self, animal): # Private Method
        x, y = animal.get_position() # Representation of the coordinates at which the animal is located.
        width, height = animal.get_size()
        for line in range(y,y+height):  # Represents the number of rows occupied by the animal.
            for place in range(x,x+width): # Represents the number of columns occupied by the animal.
                self.board[line][place] = ' '

    def can_add_animal(self, x, y, width, height):
        #A function designed to check if there is a place for an animal on the board.
        i = 0
        for line in range(y,y+height):
            for place in range(x,x+width):
                if self.board[line][place] == '*':
                    i = i + 1
        if i == 0:
            return True
        else:
            return False

    def add_animal(self, name, age, x, y, directionH, directionV, animaltype): #Adds the animal to the aquarium.
        if animaltype not in ['scalar', 'molly', 'shrimp', 'ocypode']:
            raise InvalidAnimalType(f'Error: "{animaltype}" is an invalid animal type. The valid animal types are: molly, scalar, ocypode, shrimp.')
            #Raises an error if attempting to place an animal in a location outside the aquarium or on its corners.
        if x <= 0:
            x = 1
        elif x >= self.aqua_width:  # Too big
            x = self.aqua_width - 1
        if y <= 2:
            y = 3
        elif y >= self.aqua_height:  # Too big
            y = self.aqua_height - 1

        if animaltype == 'shrimp' or animaltype == 'ocypode':
            # The animals from the crab family must be placed on the aquarium floor. If there's no need to insert them,
            # they should be placed at the nearest point as follows:
            traget_x = self.aqua_width - 1 - 7
            if x >= traget_x:
                x = traget_x

            if animaltype == 'shrimp':
                target_y = self.aqua_height - 1 - 3
                y = target_y
                if self.can_add_animal(x,y,7,3) == True:
                    animal = Shrimp(name, age, x, y, directionH)
                    self.animals.append(animal)
                    self.__insert_animal_to_board(animal)
                else:
                    raise NotAvailablePlace('Exceptions.NotAvailablePlace')

            elif animaltype == 'ocypode':
                target_y = self.aqua_height - 1 - 4
                y = target_y
                if self.can_add_animal(x,y,7,4) == True:
                    animal = Ocypode(name, age, x, y, directionH)
                    self.animals.append(animal)
                    self.__insert_animal_to_board(animal)
                else:
                    raise NotAvailablePlace('Exceptions.NotAvailablePlace')

        else:   # Fish
            # Fish cannot be located on the floor or at the waterline. They should be placed accordingly as needed.
            target_x = self.aqua_width - 1 - 8
            if x > target_x:
                x = target_x

            if animaltype == 'scalar':
                target_y = self.aqua_height - 5 - 5
                if y > target_y:
                    y = target_y
                if self.can_add_animal(x, y, 8, 5) == True:
                    animal = Scalar(name, age, x, y, directionH,directionV)
                    self.animals.append(animal)
                    self.__insert_animal_to_board(animal)
                else:
                    raise NotAvailablePlace('Exceptions.NotAvailablePlace')

            elif animaltype == 'molly':
                target_y = self.aqua_height - 5 - 3
                if y > target_y:
                    y = target_y
                if self.can_add_animal(x, y, 8, 5) == True:
                    animal = Molly(name, age, x, y, directionH,directionV)
                    self.animals.append(animal)
                    self.__insert_animal_to_board(animal)
                else:
                    raise NotAvailablePlace('Exceptions.NotAvailablePlace')

    def __kill_animal(self, animal):  # Private Method
        # Removes the animal, prints accordingly, and deletes it from the board.
        if animal.starvation() or animal.die():
            self.animals.remove(animal)
            self.__delete_animal_from_board(animal)

    def next_step(self):
        # The function represents the movement of animals in the aquarium.
        self.step = self.step + 1

        for animal in self.animals: #Checks if there are animals to kill.
            self.__kill_animal(animal)

        if self.step % 10 == 0:
            for animal in self.animals:
                animal.dec_food()
                animal.inc_age()

        bottom_line = []
        water_line = []
        board = []
        for i in range(self.aqua_height):
            row = [' '] * self.aqua_width
            board.append(row)
        for i in range(self.aqua_width):
            water_line.append('~')
            bottom_line.append('_')

        board[2] = water_line
        board[-1] = bottom_line
        index = [0, -1]  # לשנות איבר ראשון ואחרון
        for line in range(len(board)):
            for i in index:
                board[line][i] = '|'
        board[-1][0], board[-1][-1] = '\\', '/'

        self.board = board

        for i in range(len(self.animals)):
            animal = self.animals[i]
            x, y = animal.get_position()
            directionH = animal.get_directionH()
            width, height = animal.get_size()

            if isinstance(animal, Fish):
                directionV = animal.get_directionV()
                if (x <= 1 and directionH == 0) or (x + animal.get_size()[0] >= self.aqua_width - 1 and directionH == 1):
                    # Checks if the animal needs to change direction.
                    animal.set_directionH(1 - directionH)
                if (y <= 3 and directionV == 1) or (y >= (self.aqua_height - 5 - height) and directionV == 0):
                    # Checks if the animal needs to change direction.
                    animal.set_directionV(1 - directionV)

            elif isinstance(animal, Crab):
                if (x <= 1 and directionH == 0) or (x + animal.get_size()[0] >= self.aqua_width - 1 and directionH == 1):
                    # Checks if the animal needs to change direction.
                    animal.set_directionH(1 - directionH)
                for animal2 in self.animals[i:]:
                    if isinstance(animal2, Crab):
                        # Refers to the case where crabs collide or may collide.
                        x_animal2, y_animal2 = animal2.get_position()
                        directionH_animal2 = animal2.get_directionH()

                        if directionH == 0 and directionH_animal2 == 1:
                            if (x - 7 - x_animal2) == 0 or (x - 7 - x_animal2) == 1:
                                animal.set_directionH(1 - directionH)
                                animal2.set_directionH(1 - directionH_animal2)
                        elif directionH == 1 and directionH_animal2 == 0:
                            if (x_animal2 - 7 - x) == 0 or (x_animal2 - 7 - x) == 1:
                                animal.set_directionH(1 - directionH)
                                animal2.set_directionH(1 - directionH_animal2)

            animal.move()
            self.__insert_animal_to_board(animal)

    def several_steps(self, steps):
        while steps > 0:
            self.next_step()
            steps = steps - 1







