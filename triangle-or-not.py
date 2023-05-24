def triangle(a,b,c):
    if (a==b)and(b==c)and(c==a):
        print("it is an equilateral triangle")
    elif(a==0)or(b==0)or(c==0):
        print("it does not form a triangle")
    elif(a==b)or(b==c)or(c==a):
        print("it is an isosceles triangle")
    elif(a**2==b**2+c**2)or(b**2==a**2+c**2)or(c**2==a**2+b**2):
        print("it is a right angled triangle")
    else:
        print("it is a scalene triangle")
        
a=int(input("enter side a:"))
b=int(input("enter side b:"))
c=int(input("enter side c:"))
triangle(a,b,c)
print(triangle)