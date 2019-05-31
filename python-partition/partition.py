import time
import sys
import heapq
import math
from Queue import LifoQueue
import numpy as np

class DataPartition(object):
    def __init__(self, data, num_groups=2):
        self.data = data
        self.num_groups = num_groups

    def greedy_partition(self):
        groups = [[] for i in xrange(self.num_groups)]
        for n in sorted(self.data, reverse=True):
            groups.sort(key=lambda x: sum(x))
            groups[0].append(n)
        return [sum(g) for g in groups]

    def KK_partition(self): # Karmarkar-Karp heuristic
        pairs = LifoQueue()
        group1, group2 = [], []
        heap = [(-1*i, i) for i in self.data]
        heapq.heapify(heap)
        while len(heap) > 1:
            i, labeli = heapq.heappop(heap)
            j, labelj = heapq.heappop(heap)
            pairs.put((labeli, labelj))
            heapq.heappush(heap, (i-j, labeli))
        group1.append(heapq.heappop(heap)[1])
        while not pairs.empty():
            pair = pairs.get()
            if pair[0] in group1:
                group2.append(pair[1])
            elif pair[0] in group2:
                group1.append(pair[1])
        return [sum(group1), sum(group2)]

    def dp_partition(self):
        n = len(self.data)
        k = sum(self.data)
        s = int(math.floor(k/2))
        p = np.zeros((s+1, n+1))
        p[0] = 1
        for i in xrange(1, s+1):
            for j in xrange(1, n+1):
                if i - self.data[j-1] >= 0:
                    p[i][j] = p[i][j-1] or p[i-self.data[j-1]][j-1]
                else:
                    p[i][j] = p[i][j-1]
        return p[s][n]

if __name__ == '__main__':
    data_file = sys.argv[1]
    num_groups = int(sys.argv[2]) # currently only num_groups=2 is supported
    with open(data_file, "rb") as f:
        data = eval(f.read())
    dp = DataPartition(data, num_groups)
    algorithms = filter(lambda x: x.endswith("_partition"), dir(dp))
    for alg in algorithms:
        print "******************"
        start = time.time()
        print getattr(dp, alg)()
        print alg, (time.time() - start)*1000

