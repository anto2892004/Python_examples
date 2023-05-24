v = int(input("enter the speed"))
t = int(input("enter the temperature"))
ch = 13.12+0.6215*t-11.37*v**0.16+0.3965*t*v**0.16
print("the wind chill index is: ",ch)