import sys
def check_prime(num) :
    if (num>0) :
        sq = int(num ** 0.5)
        j =0
        for i in range(2,sq+1) :
            if num % i == 0:
                j =1
                return False
            else:
                continue
        if j == 0 :
            return True
    elif (num<0) :
        print "invalid negative number"
    else :
        print "zero is neither prime nor composite"

num1 = int(input("enter the number u want to check if prime"))
val = check_prime(num1)
if val is True :
    print("prime")
elif val is False :
    print("not prime")

N = int(input("enter the number below which you want to produce the prime numbers"))
for i in range(N) :
    if i == 2 or i == 3 or i == 5:
        print(i)
    elif i == 1 or i == 0:
        continue
    else :
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            continue
        else :
            val = check_prime(i)
            if val is True :
                print(i)
            else :
                continue
