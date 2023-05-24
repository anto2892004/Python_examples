year = int(input("enter the year of birth"))
c_year=int(input("enter the current year"))
age = c_year - year
a_fare = 1020
if age>=60:
    fare = (a_fare*20)/100
    d_fare = a_fare - fare
    print("the discount fare is:",d_fare)