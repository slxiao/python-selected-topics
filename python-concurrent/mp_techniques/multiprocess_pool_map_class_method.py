import multiprocessing
import os

def proxy_print_task(args):
    print args
    cls_inst, task = args[0], args[1]
    cls_inst.print_task(task)

class PrintTask(object):
    def __init__(self):
        self.time = 111
        self.tasks = [(self,'Alice'), (self,'Bob'), (self,'Cat'), (self, 'Dog')]

    def print_task(self, task):
        print task, 'done in process %s' % os.getpid()
        print self.time

    def print_task_multiprocessing(self):
        multiprocessing.Pool(4).map(proxy_print_task, self.tasks)

pt = PrintTask()
pt.print_task_multiprocessing()


