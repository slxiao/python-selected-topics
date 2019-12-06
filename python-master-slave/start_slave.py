import sys
import signal

import gevent

from client import Client
from slave import SlaveRunner


def _stop_gracefully(handler):
    def _wrapper(sig_num, frame):
        sys.stderr.write('stop the process gracefully...')
        handler()
        sys.exit()

    signal.signal(signal.SIGINT, _wrapper)

def start_slave(master_ip="127.0.0.1", master_port=9901):
    sys.stderr.write('nbsadmin slave register to %s:%d\n' % (master_ip, master_port))
    task_runner = SlaveRunner(Client(master_ip, master_port))
    _stop_gracefully(task_runner.stop)
    task_runner.loop()

if __name__ == "__main__":
    start_slave()
    