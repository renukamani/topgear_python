print("addition")
a = int(input("enter the first number"))
b = int(input("enter the second number"))
a += b
print "addition output: ",a
print("subtraction")
a = int(input("enter the first number"))
b = int(input("enter the second number"))
a -= b
print "subtraction output: ",a
print("multiplication")
a = int(input("enter the first number"))
b = int(input("enter the second number"))
a *= b
print "multiplication output: ",a
print("division")
a = int(input("enter the first number"))
b = int(input("enter the second number"))
if (b==0) :
    print("the second number cannot be zero")
else :
    a /= b
    print "Division output: ",a
print("modulus")
a = int(input("enter the first number"))
b = int(input("enter the second number"))
if (b==0) :
    print("the second number cannot be zero")
else :
    a %= b
    print "modulus output: ",a
print("exponent")
a = int(input("enter the first number"))
b = int(input("enter the second number"))
a **= b
print "exponential output: ",a
print("floor division")
a = int(input("enter the first number"))
b = int(input("enter the second number"))
if (b==0) :
    print("the second number cannot be zero")
else :
    a //= b
    print "floor division output: ",a
