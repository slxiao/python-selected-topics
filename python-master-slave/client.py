import socket
import uuid

import zmq.green as zmq

from basesocket import BaseSocket 


class Client(BaseSocket):
    def __init__(self, host='127.0.0.1', port=12305):
        self._id = socket.gethostname() + '_' + uuid.uuid1().get_hex()
        context = zmq.Context()
        self.receiver = context.socket(zmq.SUB)
        self.receiver.connect('tcp://%s:%i' % (host, port + 1))
        self.receiver.setsockopt(zmq.SUBSCRIBE, b'')

        self.sender = context.socket(zmq.PUSH)
        self.sender.connect('tcp://%s:%i' % (host, port))

    def get_id(self):
        return self._id