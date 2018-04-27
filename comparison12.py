lst = list()
for i in range(10) :
    lst.append(int(input("enter a number")))
avg = sum(lst)/10
great_count = 0
low_count = 0
equal_count = 0
for item in lst:
    if item > avg :
        great_count += 1
    elif item < avg :
        low_count += 1
    else :
        equal_count += 1
print("count of numbers greater than average: ",great_count)
print("count of numbers lower than average: ",low_count)
print("count of numbers equal to average: ",equal_count)
