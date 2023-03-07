l=[33,55,77,3,99]
def demo_fun(n):
    if n>=50:
        return True
    else:
       return False
data=list(filter(demo_fun,l))
print(data)