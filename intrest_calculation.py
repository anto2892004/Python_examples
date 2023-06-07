def intrest_cal(pa):
    name =input("enter the name:")
    age =int(input("enter the age:"))
    gender =input("enter the gender")
    if age>60:
        intrest = 12*pa/100
        print("the intrest for senior citizen is :",intrest)
    if gender=='f':
        f_intrest=10*pa/100
        print("the female intrest is:",f_intrest)
    else:
        n_intrest =9*pa/100
        print("the jnormal intrest is ",n_intrest)
obj = intrest_cal(10000)
print(obj)