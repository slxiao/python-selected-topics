import time
import sys
from utils import do_work

if __name__ == "__main__":
    tasks = [sys.argv[1]] * int(sys.argv[2])
    start = time.time()
    [do_work(task) for task in tasks]
    print time.time() - start

