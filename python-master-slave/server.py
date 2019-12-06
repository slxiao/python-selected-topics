import zmq.green as zmq

from basesocket import BaseSocket 

class Server(BaseSocket):
    def __init__(self, host='0.0.0.0', port=12305):
        context = zmq.Context()
        self.receiver = context.socket(zmq.PULL)
        self.receiver.bind('tcp://%s:%i' % (host, port))

        self.sender = context.socket(zmq.PUB)
        self.sender.bind('tcp://%s:%i' % (host, port + 1))