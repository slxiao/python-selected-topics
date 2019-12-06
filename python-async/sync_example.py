import time

def hellworld(sleep_time):
    print('hellworld starts, then sleep for %s seconds' % sleep_time)
    time.sleep(sleep_time)
    print('hellworld ends, after sleep: %s seconds' % sleep_time)

start = time.time()
hellworld(1)
hellworld(2)
print("Running program takes: %s seconds" % (time.time() - start))