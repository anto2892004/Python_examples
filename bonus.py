salary = int(input("enter the salary"))
service = int(input("enter the service"))

if service>=10:
    bonus = (salary*10)/100
    salary2 = salary+bonus
    print("the new salary of the employess above 10 years is :",salary2)

elif service>=6 and service<10:
    bonus = (salary*8)/100
    salary2 = salary+bonus
    print("the new salary of the employees above 6 years is :",salary2)

elif service<6:
    bonus = (salary*5)/100
    salary2 = salary+bonus
    print("the new salary for the employees less than 6years is :",salary2)