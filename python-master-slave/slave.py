import sys
import time
import gevent

from message import Message
from baserunner import BaseRunner


class SlaveRunner(BaseRunner):
    where = 'slave'

    def __init__(self, client):
        super(BaseRunner, self).__init__()
        self._client = client
        self._id = self._client.get_id()

    def loop(self):
        self.send_to_master('register_slave')

        # infinite loop for slave to handle tasks, it will stop until got stop message
        def _handle_operation(msg):
            print("received message %s from slave %s" % (msg.type, msg.node_id))
            getattr(self, 'on_%s' % msg.type)(msg)

        while True:
            msg = self._client.recv()
            if msg.node_id not in (None, self._id):
                continue
            gevent.spawn(_handle_operation, msg)

    def send_to_master(self, msg_type, msg_data=None):
        print("send message %s to master" % msg_type)
        self._client.send(Message(msg_type, msg_data, self._id))

    def on_operation_start(self, msg):
        ''' execute the specified operation '''
        result = self._execute(*msg.data)
        self.send_to_master("receive_result", result)

    def on_cancel(self, msg):
        self.cancel()

    def on_stop(self, msg):
        sys.stderr.write('got stop message, close slave ...')
        self.stop()

    def stop(self):
        self._client.close()