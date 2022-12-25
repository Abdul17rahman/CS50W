#This is a decorator function that is going to announce a funct.

def announce(f):
    def wrapper():
        print("About to run a function")
        f()
        print("Done running function")
    return wrapper()

#To add a decorator on a function we use the @ symbol
@announce
def hello():
    print("hello, world")

