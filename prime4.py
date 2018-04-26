import sys
num = int(input("enter a number"))
sq = int(num ** 0.5)
print sq
for i in range(2,sq+1) :
    if num % i == 0:
        sys.exit("not prime")
    else:
         continue
print("prime")
