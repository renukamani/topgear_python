nos = list()
for i in range(3) :
    nos.append(int(input("enter the number")))
if nos[0] > nos[1] and nos[0] > nos[2] :
    print ("the greatest number is:"+str(nos[0]))
elif nos[1] > nos[0] and nos[1] > nos[2] :
    print ("the greatest number is:"+str(nos[1]))
else :
    print("the greatest number is:"+str(nos[2]))
