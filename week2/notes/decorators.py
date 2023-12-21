def butt(f):
    def wrapper():
        print("About to run function")
        f()
        print("Done with the function")
    return wrapper

@butt
def hello():
    print("Hello, world!")

hello()