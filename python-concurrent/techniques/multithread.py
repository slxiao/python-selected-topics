import threading
import time
import sys
from Queue import Queue
from utils import do_work

pending_tasks = Queue()

def do_work_from_queue():
    while True:
        do_work(pending_tasks.get())
        pending_tasks.task_done()

if __name__ == "__main__":
    tasks = [sys.argv[1]] * int(sys.argv[2])
    num_threads = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    [pending_tasks.put(task) for task in tasks]
    start = time.time()
    for i in range(num_threads):
        t = threading.Thread(target=do_work_from_queue)
        t.daemon = True
        t.start()
    pending_tasks.join()
    print time.time() - start
