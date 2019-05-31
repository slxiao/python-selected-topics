import multiprocessing
import os

def print_task(task):
    task1, task2 = task[0], task[1]
    print task1, task2, 'done in process %s' % os.getpid()

tasks = [['Alice']*2, ['Bob']*2, ['Cat']*2, ['Dog']*2]

multiprocessing.Pool(4).map(print_task, tasks)

print 'End tasks'


