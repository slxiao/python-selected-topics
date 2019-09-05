class MyContext(object):
    def __init__(self):
        print("init context")

    def __enter__(self):
        print("enter context")
    
    def __exit__(self, type, value, traceback):
        print("exit context")


if __name__ == "__main__":
    print("before with")
    with MyContext():
        print("with body")
    print("after with")
