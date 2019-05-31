import multiprocessing
import os

def proxy_print_task(cls_inst, task):
    cls_inst.print_task(task)

class PrintTask(object):
    def __init__(self):
        self.tasks = ['Alice', 'Bob', 'Cat', 'Dog']

    def print_task(self, task):
        print task, 'done in process %s' % os.getpid()

    def print_task_multiprocessing(self):
        pool = multiprocessing.Pool(processes=4)
        for i in range(len(self.tasks)):
            pool.apply_async(proxy_print_task, args=(self, self.tasks[i], ))
        pool.close()
        pool.join()
        print 'End tasks'

pt = PrintTask()
pt.print_task_multiprocessing()


