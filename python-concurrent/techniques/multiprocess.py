import time
from multiprocessing import Pool, cpu_count
import sys
from utils import do_work

if __name__ == "__main__":
    tasks = [sys.argv[1]] * int(sys.argv[2])
    num_workers = int(sys.argv[3]) if len(sys.argv) > 3 else cpu_count()
    pool = Pool(num_workers)
    start = time.time()
    pool.map(do_work, tasks)
    print time.time() - start
