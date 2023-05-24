start = int(input("enter the start value"))
stop = int(input("enter the stop value"))
for i in range(start,stop):
    if i>1:
        for x in range(2,i):
            if(i%x)==0:
                break
        else:
            print(i)