def demo(x):
    return lambda a,b:a*b*x
# 10 goes to x place
d=demo(10)
# calling anonymous function

print(d(4,2))
print(d(8,2))
##################################################
print("Single parameter")
def demo1(x):
    return lambda a:a*x
d=demo1(2)
print(d(3))