n = [1,2,3,4]
a = int(input("enter the number to be found:"))
p_count = []
n_count = []
c = len(n)
for i in range(0,c):
    if n[i]==a:
        p_count.append(i)
        n_count.append(-len(n)+i)
print(p_count)
print(n_count)
