def swap(a,b):
    c = b
    b = a
    a = c
    return a,b

x = 10
y = 20
print("before swap",x,y)

afterSwap = swap(x,y)
print("after swap",afterSwap)