from math import sqrt
def p_square(x):
    sq_root=int(sqrt(x))
    check = (sq_root*sq_root)
    if check==x:
        print("it is a perfect sqare")
    else:
        print("it is not a perfect square")
obj=p_square(36)
print(obj)