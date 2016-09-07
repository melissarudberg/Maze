from Maze import *
import random
import turtle
import unittest

class testMaze(unittest.TestCase):
    """
    This class inherits from a class called TestCase which is
    defined in the unittest module.

    When you inherit from a class, you get all the methods that are
    defined in that class for free.

    Since this is a TestCase class, calling unittest.main() will automatically
    run any of the funtions that start with the word 'test'
    """
    
    def setUp(self):
        """
        this will check to see if we have a maze class but as soon
        as setUp is run, we will see a failure so we really don't need
        to do anything here
        """

        pass
    
#    def testScreenExists(self):
#        assert type(self.m.s) == turtle._Screen

unittest.main()
    
