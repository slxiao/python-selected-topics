import sys
import signal

from server import Server
from master import MasterRunner


def _stop_gracefully(handler):
    def _wrapper(sig_num, frame):
        sys.stderr.write('stop the process gracefully...')
        handler()
        sys.exit()

    signal.signal(signal.SIGINT, _wrapper)

def start_master(master_port):
    sys.stderr.write('nbsadmin master RPC is listening to 0.0.0.0:%d\n' % master_port)
    task_runner = MasterRunner(Server('0.0.0.0', master_port))
    _stop_gracefully(task_runner.stop)
    task_runner.loop()

if __name__ == "__main__":
    start_master(9901)
    