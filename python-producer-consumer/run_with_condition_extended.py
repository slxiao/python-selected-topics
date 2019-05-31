from threading import Thread, Condition
import time
import random

condition = Condition()
queue = []

MAX_NUM = 10

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM:
                print "Queue full, producer is waiting"
                condition.wait()
                print "Space in queue, consumer notified producer"
            num = random.choice(nums)
            queue.append(num)
            print "produced: ", num
            condition.notify()
            condition.release()
            time.sleep(random.random())

class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print "nothing in queue, consumer is waiting"
                condition.wait()
                print "producer added sth and notified the consumer"
            num = queue.pop(0)
            print "consumed: ", num
            condition.notify()
            condition.release()
            time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()
