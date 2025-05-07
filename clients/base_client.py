import zmq
import json


class BaseZmqClient:
    def __init__(self, server_address):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(server_address)
    
    def send_request(self, request_data):
        self.socket.send_string(json.dumps(request_data))
        response = self.socket.recv_string()
        return json.loads(response)
    
    def close(self):
        self.socket.close()
        self.context.term()
