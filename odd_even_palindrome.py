a = int(input("enter a number: "))
if a%2!=0:
    for i in range(1,a+1):
        fact = 1
        fact = fact*i 
    print("the factorial is:",fact)
    print("the length of the factorial:",len(str(fact)))
else:
    temp = a 
    reverse = 0
    while temp>0:
        rem = temp%10
        reverse = (reverse*10)+rem 
        temp = temp//10
    if a==reverse:
        print("palindrome")
    else:
        print("not a palindrome")
