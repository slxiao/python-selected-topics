import multiprocessing
import os

def print_task(task1, task2):
    print task1, task2, 'done in process %s' % os.getpid()

tasks = ['Alice', 'Bob', 'Cat', 'Dog']

pool = multiprocessing.Pool(processes=4)
for i in range(len(tasks)):
    pool.apply_async(print_task, args=(tasks[i],tasks[i], ))

pool.close()

pool.join()

print 'End tasks'


