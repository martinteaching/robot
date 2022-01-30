# Filename: must being with 'test' in order to be picked up by python unittest module.
import unittest
from robot import Robot

# Inherit from 'TestCase', so that we can (A) access some useful functions that have already been defined in the parent class (e.g. 'assertEqual') and (B) override (re-define and replace the functionality of) certain functions that are going to be called when running the test (e.g. setUp).
class TestRobot(unittest.TestCase):
    
    # We know a function with this named will be called when the object is executed by the unittest module, so if we 'intercept' this call by adding a function with the same name, we can automatically run our code instead.
    # Note: some library classes break typical Python naming conventions, e.g. camelCase instead of snake_case.
    def setUp(self):
        # Define a storage space within the object of this class to store a copy of our robot code. This can then be subsequently accessed from our test methods.
        self._robot = Robot();
    
    # Test: Ensure the robot can move down (backwards) (standard case)
    # Test method must begin with the word 'test' in order to be picked up
    def testMoveDown(self):
        # Move a normal amount
        self._robot.move(0, -3);
        self.assertEqual(self._robot.get_y(), -3);
    
    # Test: Ensure the robot can move a large amount left (edge case)
    def testMoveLarge(self):
        # Move a large amount
        self._robot.move(-100000, 0);
        self.assertEqual(self._robot.get_x(), -100000);
    
    # Test: Ensure the robot does move (negative case)
    def testNegative(self):
        self._robot.move(3, 3);
        # It should *not* be the case that the robot *doesn't* move
        self.assertNotEqual(self._robot.get_x(), 0);
        self.assertNotEqual(self._robot.get_y(), 0);
        
