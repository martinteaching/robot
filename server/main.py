from robot import Robot
# Import HTTPServer, which will actually run and receive HTTP requests.
from http.server import HTTPServer
from robot_server import RobotServer

# Our new main class doesn't collect data, but instead simply start the server, which waits from input via HTTP.

# The HTTP server is powered by our handler, which is the robot server we've already written.
# In addition, we supply two bits of information that allow requests to our server to reach it: an address (identifies a machine) and a port (identifies a process running on that machine).
# Our server will then listen on this address and on this port, for requests.
# NB: 0.0.0.0 allows us to listen on all the addresses a machine has, if it has more than one. 
# Generally need to be careful listening to all addresses, but OK for now for our purposes.
server = HTTPServer(('0.0.0.0', 8888), RobotServer);

print('Listening...');
try:
  # Keep listening for requests, until interrupted.
  server.serve_forever();
# CLARIFY: Catching the exception
# A: Allows us to proceed to the server close (the interrupt is handled and passed, rather than stopping execution).
# B: Neatens things up; ensures we don't print details of the exception to the console when we exit.
except KeyboardInterrupt:
  pass;

# Neatly close down the server once it has been interrupted.
server.server_close();
