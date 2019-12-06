from message import Message


class BaseSocket(object):
    def send(self, msg):
        self.sender.send(msg.serialize())

    def recv(self):
        data = self.receiver.recv()
        return Message.unserialize(data)

    def close(self):
        self.sender.close()
        self.receiver.close()