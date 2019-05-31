from gevent import monkey
monkey.patch_all()

from gevent.pool import Pool
import gevent
import time
import sys
from utils import do_work

if __name__ == "__main__":
    tasks = [sys.argv[1]] * int(sys.argv[2])
    pool_limit = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    pool = Pool(pool_limit)
    start = time.time()
    pool.map(do_work, tasks)
    print time.time() - start
