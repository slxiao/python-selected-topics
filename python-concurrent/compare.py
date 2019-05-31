import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import re
import numpy as np
import os
import subprocess
import sys

def compare(repeat, group, step):
    techniques = filter(lambda x : x not in ["utils"], [i.split(".")[0] for i in os.listdir("./techniques")])
    tasks = {"cpu_bound" : 100000, "io_bound" : "https://gitlabe1.ext.net.nokia.com"}
    x = [step * (i + 1) for i in xrange(group)]

    for task_type, task in tasks.iteritems():
        y = {}
        for t in techniques:
            y[t] = np.zeros((repeat, group))
        for r in xrange(repeat):
            for g in xrange(1, group + 1):
                for t in techniques:
                    print "task_type: %s; repeat: %d; group: %d; technique:%s" % (task_type, r, g, t)
                    res = subprocess.check_output("python ./techniques/%s.py %s %s" % (t, task, g), shell=True)
                    y[t][r][g-1] = float(res.strip())

        for t in techniques:
            np.savetxt("./result/%s_%s_data.txt" % (task_type, t), y[t])
            y[t] = y[t].sum(0)/repeat

        d = 2000
        xlabel = 'num of tasks'
        ylabel = 'average time in seconds'
        plt.figure(1)
        styles= ["g^-", "ro-", "b+-", "y>-", "k<-"]
        for t in techniques:
            plt.plot(x, y[t], styles.pop(0), label="%s technique"%t)
        plt.legend(loc='best')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig('./result/compare_%s.png' % task_type, dpi=d)
        plt.close()

if __name__ == "__main__":
    repeat = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    group = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    step = int(sys.argv[3]) if len(sys.argv) > 3 else 1000
    compare(repeat, group, step)
