class Robot:

  # Our goal position is provided as two parameters, an X and a Y coordinate.
  # Adding `self` allows us to access data that is held in the copy (instance) of the class (the object).
  # Even if not used, explicitly states that this method needs to be accessed by creating an instance of this code as an object.
  def move(self, x, y):
    # We know our robot always starts back at position 0, so represent this here.
    # Double underscore indicates that this is *not* something that should be accessed from outside the class (a private property), which is good coding practice.
    # This is something that it would be good to include in something called a 'constructor', something that runs every time we make an instance of a class.
    self._x = 0;
    self._y = 0;
    # We want to track the robot's path, so define a variable that we can use to incrementally construct the path.
    path = '';
    # We know the robot has more steps to make while its current position is not equal to the goal position, on either the X or Y axis. We represent this as a repeating loop.
    while(self._x != x or self._y != y):
      # *Decrease* the robot's X position by 1 if the target point is still to the 'left' of it; *increase* the robot's X position by 1 if the target position is still to the 'right' of it.
      self._x = self._x-1 if self._x>x else (self._x+1 if self._x<x else self._x);
      # *Decrease* the robot's Y position by 1 if the target position is still 'below' the robot; *increase* the robot's Y position by 1 if the target position is still 'above' the robot.
      self._y = self._y-1 if self._y>y else (self._y+1 if self._y<y else self._y);
      # For each step made, record this by adding to the contents of our path variable (to be returned later).
      path += '(' + str(self._x) + ',' + str(self._y) + ') ';
      print('x: '+str(self._x)+' y: '+str(self._y));
    return path;

  # 'Accessor methods', for both the X and Y coordinate, allow us to access the robot's position at any time.
  def get_x(self): return self._x;
  
  def get_y(self): return self._y;
