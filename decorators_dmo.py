def outer():
    print("Hello from outer function")
    def inner():
        print("Hello from inner function")
    inner()
d=outer()

###############################
def outer():
    print("Hello from outer function")
    def inner():
        print("Hello from inner function")
    return inner()
d=outer()


