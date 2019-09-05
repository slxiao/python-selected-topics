from contextlib import ContextDecorator

class mycontext(ContextDecorator):
    def __enter__(self):
        print('Starting')
        return self

    def __exit__(self, *exc):
        print('Finishing')
        return False

@mycontext()
def function():
    print('The bit in the middle')

function()

with mycontext():
    print('The bit in the middle')