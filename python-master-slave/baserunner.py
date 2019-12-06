
import signal
import math 
import time 

from gevent.event import Event

import suites

class BaseRunner(object):
    ''' base runner class '''
    where = None  # where runner to run

    @property
    def agents(self):
        ''' used for agents page '''
        raise RuntimeError('unimplemented!')

    def cancel(self):
        ''' cancel last execution '''
        signal.alarm(1)  # set alarm signal

    def execute(self, operation, amount, ratio, loop, interval, kwargs):
        raise RuntimeError('unimplemented!')

    def _execute(self, operation, number):
        ''' real execution
        '''
        return getattr(suites, operation)(number)
        

    def stop(self):
        ''' stop the whole runner '''
        raise RuntimeError('unimplemented!')
