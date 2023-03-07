old_price=[20,22,23,44,55,66,77]
rs=5
def add_price(no):
    return no+rs
new_price=map(add_price,old_price)
print(list(new_price))

# lambda function


new_price1=list(map(lambda n:n+rs,old_price))
print(list(new_price1))
