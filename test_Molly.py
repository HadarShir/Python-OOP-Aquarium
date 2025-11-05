from unittest import TestCase
from Molly import *

class TestMolly(TestCase):
    #A test file that includes functions with meaningful names explaining each test.
    def test_init_with_invalid_input(self):
        with self.assertRaises(InvalidInputException):
            Molly(1, 50, 3, 7, 0, 1)
            Molly('', 50, 3, 7, 0, 1)
            Molly('molly', 0.6, 3, 7, 0, 1)
            Molly('molly', -1, 3, 7, 0, 1)
            Molly('molly', 121, 3, 7, 0, 1)
            Molly('molly', 50, 3.1, 7, 0, 1)
            Molly('molly', 50, -3, 7, 0, 1)
            Molly('molly', 50, 3, -7, 0, 1)
            Molly('molly', 50, 1, 7.1, 0, 1)
            Molly('molly', 50, 3, 7, 2, 1)
            Molly('molly', 50, 3, 7, 0, 2)

    def test_init_with_valid_input(self):
        molly = Molly('molly', 50, 3, 7, 0, 1)
        self.assertEqual('molly', molly.name, msg='Error in name')
        self.assertEqual(50, molly.age, msg='Error in age')
        self.assertEqual(3, molly.x, msg='Error in x')
        self.assertEqual(7, molly.y, msg='Error in y')
        self.assertEqual(0, molly.directionH, msg='Error in directionH')
        self.assertEqual(1, molly.directionV, msg='Error in directionV')
        self.assertEqual(10, molly.food, msg='Error in food')
        self.assertEqual(8, molly.width, msg='Error in width')
        self.assertEqual(3, molly.height, msg='Error in height')

    def test_str(self):
        molly = Molly('molly', 50, 3, 7, 0, 1)
        expected_str = 'The molly molly is 50 years old and has 10 food.'
        self.assertEqual(expected_str, str(molly), msg='Error in str')

    def test_position(self):
        molly = Molly('molly', 50, 1,1, 1, 1)
        self.assertEqual((1, 1), molly.get_position(), msg='Error in get_position')
        molly = Molly('molly', 50, 7, 3, 1, 1)
        self.assertEqual((7, 3), molly.get_position(), msg='Error in get_position')

    def test_get_directionH(self):
        molly = Molly('molly', 50, 1, 1, 1, 1)
        self.assertEqual(1, molly.get_directionH(), msg='Error in get_directionH')
        molly = Molly('molly', 50, 1, 1, 0, 1)
        self.assertEqual(0, molly.get_directionH(), msg='Error in get_directionH')

    def test_get_directionV(self):
        molly = Molly('molly', 50, 1, 1, 1, 1)
        self.assertEqual(1, molly.get_directionV(), msg='Error in get_directionV')
        molly = Molly('molly', 50, 1, 1, 0, 0)
        self.assertEqual(0, molly.get_directionV(), msg='Error in get_directionV')

    def test_set_directionH(self):
        molly = Molly('molly', 50, 1, 1, 0, 1)
        molly.set_directionH(0)
        self.assertEqual(0, molly.get_directionH(), msg='Error in set_directionH')
        molly.set_directionH(1)
        self.assertEqual(1, molly.get_directionH(), msg='Error in set_directionH')
        molly.set_directionH(0)
        self.assertEqual(0, molly.get_directionH(), msg='Error in set_directionH')

    def test_set_directionV(self):
        molly = Molly('molly', 50, 1, 1, 1, 1)
        molly.set_directionV(1)
        self.assertEqual(1, molly.get_directionV(), msg='Error in set_directionV')
        molly.set_directionV(0)
        self.assertEqual(0, molly.get_directionV(), msg='Error in set_directionV')
        molly.set_directionV(1)
        self.assertEqual(1, molly.get_directionV(), msg='Error in set_directionV')

    def test_get_size(self):
        molly = Molly('molly', 50, 1, 1, 1, 1)
        self.assertEqual((8, 3), molly.get_size(), msg='Error in get_size')
        molly = Molly('molly', 50, 6, 7, 0, 0)
        self.assertEqual((8, 3), molly.get_size(), msg='Error in get_size')

    def test_dec_food(self):
        molly = Molly('molly', 10, 6, 7, 0, 0)
        self.assertEqual(10, molly.food, msg='Error in init food')
        molly.dec_food()
        self.assertEqual(9, molly.food, msg='Error in dec food')
        molly.dec_food()
        self.assertEqual(8, molly.food, msg='Error in dec food')
        molly.dec_food()
        self.assertEqual(7, molly.food, msg='Error in dec food')

    def test_inc_age(self):
        molly = Molly('molly', 10, 6, 7, 0, 0)
        self.assertEqual(10, molly.age, msg='Error in init age')
        molly.inc_age()
        self.assertEqual(11, molly.age, msg='Error in inc_age')
        molly.inc_age()
        self.assertEqual(12, molly.age, msg='Error in inc_age')
        molly.inc_age()
        self.assertEqual(13, molly.age, msg='Error in inc_age')

    def test_starvation(self):
        molly = Molly('molly', 10, 6, 7, 0, 0)
        self.assertEqual(False, molly.starvation(), msg='Error in starvation')
        for i in range(10):
            molly.dec_food()
        self.assertEqual(True, molly.starvation(), msg='Error in starvation')

    def test_die(self):
        molly = Molly('molly', 119, 6, 7, 0, 0)
        self.assertEqual(False, molly.die(), msg='Error in die')
        molly.inc_age()
        self.assertEqual(True, molly.die(), msg='Error in die')

    def test_get_animal(self):
        molly_left = [[" ", "*", "*", "*", "*", " ", " ", "*"],
                      ["*", "*", "*", "*", "*", "*", "*", "*"],
                      [" ", "*", "*", "*", "*", " ", " ", "*"]]

        molly_right = [["*", " ", " ", "*", "*", "*", "*", " "],
                       ["*", "*", "*", "*", "*", "*", "*", "*"],
                       ["*", " ", " ", "*", "*", "*", "*", " "]]
        molly = Molly('molly', 50, 6, 7, 0, 0)
        self.assertEqual(molly_left, molly.get_animal(), msg='Error in get_animal')
        molly.set_directionH(1)
        self.assertEqual(molly_right, molly.get_animal(), msg='Error in get_animal')

    def test_move(self):
        molly = Molly('molly', 50, 12, 22, 0, 0)
        molly.move()
        self.assertEqual((11, 23), molly.get_position())
        molly = Molly('molly', 50, 12, 22, 0, 1)
        molly.move()
        self.assertEqual((11, 21), molly.get_position())
        molly = Molly('molly', 50, 12, 22, 1, 0)
        molly.move()
        self.assertEqual((13, 23), molly.get_position())
        molly = Molly('molly', 50, 12, 22, 1, 1)
        molly.move()
        self.assertEqual((13, 21), molly.get_position())

    def test_repr(self):
        rep = '  * * * *     *\n* * * * * * * *\n  * * * *     *\n'
        molly = Molly('molly', 50, 6, 7, 0, 0)
        self.assertEqual(rep, repr(molly), msg='Error in repr')
        rep = '*     * * * *  \n* * * * * * * *\n*     * * * *  \n'
        molly = Molly('molly', 50, 6, 7, 1, 0)
        self.assertEqual(rep, repr(molly), msg='Error in repr')

    def test_add_food(self):
        molly = Molly('molly', 50, 6, 7, 0, 0)
        self.assertEqual(10, molly.food, msg='Error in init food')
        molly.add_food(10)
        self.assertEqual(20, molly.food, msg='Error in add food')
        molly.add_food(10)
        self.assertEqual(30, molly.food, msg='Error in add food')

