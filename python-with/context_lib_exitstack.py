from contextlib import ExitStack

def cleanup_resources():
    print("cleanup_resources")

with ExitStack() as stack:
    stack.callback(cleanup_resources)
    print("stack")

with ExitStack() as stack:
    stack.callback(cleanup_resources)
    print("stack")
    stack.pop_all()