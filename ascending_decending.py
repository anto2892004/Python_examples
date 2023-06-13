test_list = []
n = int(input("enter the length of the list: "))

for i in range(n):
    ele = int(input("enter the number: "))
    test_list.append(ele)

print("Original list : " + str(test_list))
flag = 0
if(test_list == sorted(test_list)):
    flag = 1
     
if (flag) :
    print("Yes, List is sorted.")
else :
    print("No, List is not sorted.")