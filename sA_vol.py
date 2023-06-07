pi=3.14
r=int(input("enter the radius:"))
h=int(input("enter the height"))
s =int(input("enter the slant height"))
def sphere():
    surface_area=4/3*pi*r*r
    volume = 4/3*pi*r*r*r
    print("the SA of the sphere is",surface_area)
    print("the volume ofthe sphere is",volume)
def cyl():
    surface_area1=(2*pi*r*r) + (2*pi*r*h)
    volume1 =pi*r*r*h 
    print("the SA of the cylinder is",surface_area1)
    print("the volume of the cyl is:",volume1)
def cone():
    surface_area2=pi*r*s + pi*r*r
    volume2 = 1/3(pi*r*r*h)
    print("the SA of the cone is",surface_area2)
    print("the volume of the cone is:",volume2)
print(sphere())
print(cyl())
print(cone())