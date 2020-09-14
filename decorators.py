def announce(f):
    def wrapper():
        print("About to run a function")
        f()
        print("Finished running the function")
    
    return wrapper


@announce
def hello():
    print("Say Hello world")

hello()