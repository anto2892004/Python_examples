e_count =0
o_count =0
for i in range(1,100):
    i =int(input("Ennter a number"))
    if i==-1:
        break
    if i%2==0:
        e_count+=1
    else:
        o_count+=1
print("the evencount is:",e_count)
print("theodd count is",o_count)