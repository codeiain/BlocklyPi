import SimpleHTTPServer
import SimpleXMLRPCServer
import robot.setMotorPower as RobotMotorPower
import robot.setSwitches as RobotSwitch
import robot.setSleep as RobotSleep

def registerRobotXmlRpcMethods(server):
    
    # Register standard XML-RPC methods.
    server.register_introspection_functions()
    
    # Register the motor power command function.
    RobotMotorPower.init()
    RobotSwitch.init()
    RobotSleep.init()
    server.register_function(RobotMotorPower.set,'setRobotMotorPower')
    server.register_function(RobotSwitch.set, 'setRobotSwitch')
    server.register_function(RobotSleep.set,'setRobotSleep')


    
    
# We define a custom server request handler, capable of both handling GET and XML-RPC requests.
class RequestHandler(SimpleXMLRPCServer.SimpleXMLRPCRequestHandler, SimpleHTTPServer.SimpleHTTPRequestHandler):
    rpc_paths = ('/RobotControlService',)

    def do_GET(self):
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)      
    
    
    
    
# Start running the server ...    
if __name__ == "__main__":
    
    # Create our XML-RPC server.using out custom request handler that is also able to serve web pages over GET.
    port = 8080
    server = SimpleXMLRPCServer.SimpleXMLRPCServer(("", port), RequestHandler)
    
    # Register the XML-RPC methods ...
    registerRobotXmlRpcMethods(server)
    
    # Start to server.
    server.serve_forever()
