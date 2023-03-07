def decor(func):
    def inner(name):
        if name=='hcl':
            print("Hello Hcl with extra functions")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("Hello",name)
wish("hcl")
wish("wipro")