"""A simple example of asyncio. This code is available from python 3.7. 
References
- history of asyncio: https://asyncio-notes.readthedocs.io/en/latest/asyncio-history.html
- asyncio: https://docs.python.org/3/library/asyncio.html
- asyncio.queue: https://docs.python.org/3.7/library/asyncio-queue.html
- producer-consumer: https://stackoverflow.com/questions/52582685/using-asyncio-queue-for-producer-consumer-flow
"""

import asyncio
import random


async def mock_worker(queue: asyncio.Queue):
    """Get items from the queue and execute tasks."""
    print(f"start worker")
    while True:
        task = await queue.get()
        queue.task_done()
        print(f"worker finished task {task}")


async def mock_receiver(queue: asyncio.Queue):
    """Make mock data and put it in the queue."""
    print(f"start receiver")
    while True:
        item = random.random()  # assume it receives any data
        await asyncio.sleep(2)
        await queue.put(item)
        print(f"receiver has put {item} in Queue")


async def main():
    """Create worker and receiver and wait until they are done."""
    queue = asyncio.Queue()

    worker = asyncio.create_task(mock_worker(queue))
    receiver = asyncio.create_task(mock_receiver(queue))

    tasks = [worker, receiver]
    await asyncio.gather(*tasks)  # wait until all tasks are done
    print("main() is done")

    
# execute!
asyncio.run(main())