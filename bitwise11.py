a = int(input("enter first number"))
b = int (input("enter second number"))
c = 0

c = a & b
print "Binary AND - Value of c is ", c

c = a | b
print "Binary OR - Value of c is ", c

c = a ^ b
print "Binary XOR - Value of c is ", c

c = ~a
print "Binary complement of first number is ", c

c = a << 2
print "binary left shift of first number is ", c

c = a >> 2
print "Binary right shift of first number is", c
