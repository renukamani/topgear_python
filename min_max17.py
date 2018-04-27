def greatest_number(lst) :
    size = len(lst)
    myHigh = lst[0]
    for item in lst :
        if myHigh < item :
            myHigh = item
        else :
            continue
    return myHigh

def smallest_number(lst) :
    size = len(lst)
    mySmall = lst[0]
    for item in lst :
        if mySmall > item :
            mySmall = item
        else :
            continue
    return mySmall

myList = list()
N = int(input("enter the count of numbers"))
for i in range(N) :
    myList.append(int(input("enter the number")))
a = greatest_number(myList)
b = smallest_number(myList)
print "greatest of numbers is: ", a
print "smallest of numbers is: ", b
