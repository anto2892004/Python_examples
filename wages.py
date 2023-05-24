name = input("enter the name: ")
age = int(input("enter the age :"))
gender = input("enter the gender: ")
days = int(input("enter the number of days: "))
if age>=18 and age<30:
    if gender=='M':
        wages = 700*days
        print("the wages of male is:",wages)
    else:
        wages = 750*days
        print("the wages of female is: ",wages)
if age>=30 and age<=40:
    if gender=='M':
        wages = 800*days
        print("the wages of male employee is :",wages)
    else:
        wages = 800*days
        print("the wages of the female employee is :",wages)



