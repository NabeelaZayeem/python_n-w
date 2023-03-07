def hello():
    print("Hello Hcl")
def call(func):
    temp=func()
    return temp
d=call(hello)
d