import sys
import time
import gevent

from message import Message
from baserunner import BaseRunner


class MasterRunner(BaseRunner):
    where = 'master'

    def __init__(self, server):
        super(BaseRunner, self).__init__()
        self._master = server
        self._clients = {}
        self._clients_cycle = self._cycle_client()

    def execute(self, operation, number):
        for client_id in self._clients:
            self.send_to_slave('operation_start', (operation, number), client_id)

    def cancel(self):
        ''' send cancel msg to all slaves '''
        self.send_to_slave('cancel')

    def loop(self):
        # infinite loop for master to handle received events
        def _handle_operation(msg):
            print("received message %s from slave %s" % (msg.type, msg.node_id))
            getattr(self, 'on_%s' % msg.type)(msg)


        while True:
            msg = self._master.recv()
            gevent.spawn(_handle_operation, msg)

    def on_register_slave(self, msg):
        self._clients[msg.node_id] = time.time()
        self.execute("calculate", 2)

    def on_receive_result(self, msg):
        self.stop()

    def stop(self):
        sys.stderr.write('stop master and all slaves ...')
        self.send_to_slave('stop')
        self._master.close()

    def send_to_slave(self, msg_type, msg_data=None, to=None):
        if to == 'any':
            to = self._clients_cycle.next()
        print("send message %s to slave %s" % (msg_type, to))
        self._master.send(Message(msg_type, msg_data, to))

    def _cycle_client(self):
        iter_clients = self._clients.iterkeys()
        while True:
            try:
                yield iter_clients.next()
            except StopIteration:
                iter_clients = self._clients.iterkeys()
