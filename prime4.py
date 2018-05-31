import sys
num = int(input("enter a number"))
if (num>0) :
    sq = int(num ** 0.5)
    for i in range(2,sq+1) :
        if num % i == 0:
            print("not prime")
            sys.exit()
        else:
             continue
    print("prime")
elif (num<0) :
    print ("please enter a positive value")
else :
    print ("the number entered is neither prime nor a non-prime")
