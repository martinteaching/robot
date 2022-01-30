from sample_server import SampleServer
from robot import Robot

# Inherit all the functions from the pre-supplied sample server class.
class RobotServer(SampleServer):
    
    # This is a method from the 'grandparent' class, BaseHTTPRequestHandler, which we receive through SampleServer, and we know is called every time the server, which this handler will power, receives an HTTP POST request.
    def do_POST(self):
        # Use a method from our helper SampleServer class (parent) to extract the data we need once a post request is made.
        post_data = self.get_post_data();
        # Create an instance of the robot class in order to process the data we receive.
        # NB: Really we should only do this once per instance.
        robot = Robot();
        # Extract the supplied X and Y coordinates from the POST request.
        # This is our 'contract' with the client; the structure they have to use in order for us to be able to understand the request.
        sent_x = post_data['x'];
        sent_y = post_data['y'];
        # Move the robot, supplying the extracted data, as we would normally.
        path = robot.move(sent_x, sent_y);
        # Again invoke an inherited method from the helper SampleServer class, in order to send a response to the POST request received, containing the path that the robot took.
        self.send_post_response(path);
