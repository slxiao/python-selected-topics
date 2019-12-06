import time
import asyncio

async def hellworld(sleep_time):
    print('hellworld starts, then sleep for %s seconds' % sleep_time)
    await asyncio.sleep(sleep_time)
    print('hellworld ends, after sleep: %s seconds' % sleep_time)

loop = asyncio.get_event_loop()

start = time.time()
loop.run_until_complete(asyncio.gather(hellworld(1), hellworld(2)))
print("Running program takes: %s seconds" % (time.time() - start))
