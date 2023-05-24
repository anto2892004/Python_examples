def volume(radius,height):
    pi = 3.14
    return pi*radius*radius*height
obj = volume(10,20)
print("the volume is :",obj)

def surface(radius1,height1):
    pi = 3.14
    return ((2*pi*radius1)*height1)+ ((pi*radius1**2)*2)
obj1 = surface(30,10)
print("the surface is :",obj1)