from contextlib import contextmanager

@contextmanager
def managed_resource(*args, **kwds):
    # Code to acquire resource, e.g.:
    print("acquire resource")
    resource = 1
    try:
        yield resource
    finally:
        # Code to release resource, e.g.:
        print("release resource")


if __name__ == "__main__":
    print("before with")
    with managed_resource(timeout=3600) as resource:
        print("with body")
        print(resource)
    print("after with")
