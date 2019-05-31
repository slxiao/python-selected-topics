import multiprocessing
import os

class PrintTask(object):
    def __init__(self):
        self.tasks = ['Alice', 'Bob', 'Cat', 'Dog']

    def print_task(self, task):
        print task, 'done in process %s' % os.getpid()

    def print_task_multiprocessing(self):
        multiprocessing.Pool(4).map(self.print_task, self.tasks)

pt = PrintTask()
pt.print_task_multiprocessing()


