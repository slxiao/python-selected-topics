from threading import Thread, Lock
import time
import random

queue = []
lock = Lock()

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            num = random.choice(nums)
            lock.acquire()
            queue.append(num)
            print "produced: ", num
            lock.release()
            time.sleep(random.random())

class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            lock.acquire()
            if not queue:
                print "nothing in queue, but try to consume"
            num = queue.pop(0)
            print "consumed: ", num
            lock.release()
            time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()
