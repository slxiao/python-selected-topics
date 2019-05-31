import multiprocessing
import os

def print_task(task):
    print task, 'done in process %s' % os.getpid()

tasks = ['Alice', 'Bob', 'Cat', 'Dog']

multiprocessing.Pool(4).map_async(print_task, tasks)

print 'End tasks'


