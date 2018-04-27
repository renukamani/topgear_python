def greatest_number(lst) :
    size = len(lst)
    myHigh = lst[0]
    for item in lst :
        if myHigh < item :
            myHigh = item
        else :
            continue
    return myHigh

myList = list()
for i in range(4) :
    myList.append(int(input("enter the number")))
a = greatest_number(myList)
print "greatest of 4 numbers is: ", a
myList.append(int(input("enter the fifth number")))
a = greatest_number(myList)
print "greatest of 5 numbers is: ", a
