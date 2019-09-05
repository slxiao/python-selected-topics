class MyContext(object):
    def __init__(self):
        print("init context")

    def __enter__(self):
        print("enter context")
        return self
    
    def __exit__(self, type, value, traceback):
        print("exit context")


if __name__ == "__main__":
    print("before with")
    with MyContext() as context:
        print("with body")
        print(context)
    print("after with")
    