# Import class Robot from the robot module
from robot import Robot

# Create a new copy (instance) of our class - an object.
robot = Robot();

# Because we need two integers, keep looping until the user gives us those two integers (rather than, say, one or more strings).
while True:
  try:
    # Cast each input as an integer, and if either fails, the exception will simply bring us back to the top of the loop.
    x = int(input('Enter target X position: '));
    y = int(input('Enter target y position: '));
    # If we succeed in converting two integers from the input, break from (exit) the loop. 
    break;
  # Exceptions can have different 'types'. This is the type of exception we know is 'thrown' when trying to convert a non-integer string to an integer, so we explicitly listen for it.
  except ValueError:
    # We need to list something for the exception to adhere to Python's rules, but we don't need to do anything (we'll go back to the top of the loop automatically), so just add pass, which does nothing.
    pass;

# Keep moving the robot until it reaches the target position.
path = robot.move(x,y);
# Report the robot's path to the user.
print('Robot path: ' + str(path));
# Report on the robot's final position.
print('Final position: (' + str(robot.get_x()) + ',' + str(robot.get_y()) + ').');
