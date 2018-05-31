no1 = int(input("enter first number"))
no2 = int(input("enter second number"))
print("sum of two numbers is:"+str(no1+no2))
print("difference between the two numbers is:"+str(abs(no1-no2)))
print("multiplication of two numbers is:"+str(no1*no2))
if no2 == 0 :
    print("the divisor is invalid, cannot take the value zero")
else :
    d = float(no1/no2)
    print("division of two numbers is:"+str(d))
