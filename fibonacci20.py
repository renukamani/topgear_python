def generate_fibonacci(num) :
    fib = list()
    fib.append(0)
    fib.append(1)
    for i in range(2,num) :
        fib.append(fib[i-1] + fib[i-2])
    return fib

N = int(input("enter the number"))
print(generate_fibonacci(N))

Max = int(input("enter the max number in series"))
fib = list()
if (Max == 1) :
    print "0"
else :
    fib.append(0)
    fib.append(1)
    num = fib[0] + fib[1]
    while (num<Max) :
        fib.append(num)
        num = fib[-1] + fib[-2]
    print fib
