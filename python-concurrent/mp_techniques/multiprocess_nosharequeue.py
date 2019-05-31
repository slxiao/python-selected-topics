import multiprocessing
from Queue import Queue
import os
import time

def print_task(task_queue):
    while not task_queue.empty():
        task = task_queue.get_nowait()
        print task, 'done in process %s' % os.getpid()

tasks = ['Alice', 'Bob', 'Cat', 'Dog']

task_queue = Queue()
for task in tasks:
    task_queue.put(task)

processes = []

num_of_processes = 2

for i in xrange(num_of_processes):
    p = multiprocessing.Process(target=print_task, args=(task_queue, ))
    processes.append(p)
    p.start()

print 'End tasks, processes do not share task_queue'

