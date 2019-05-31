import multiprocessing
import os
import time

def print_task(task):
    time.sleep(1)
    print task, 'done in process %s' % os.getpid()

tasks = ['Alice', 'Bob', 'Cat', 'Dog']

processes = []

for i in xrange(len(tasks)):
    p = multiprocessing.Process(target=print_task, args=(tasks[i], ))
    processes.append(p)
    p.start()

print 'End tasks'

