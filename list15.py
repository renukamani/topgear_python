names = list()
for i in range(5) :
    names.append(raw_input("enter name").lower())
name = raw_input("enter the name u want to check").lower()
if name in names :
    print("yes - using in operator")
else :
    print("no - using in operator")
i = 0
for item in names :
    if item.lower() == name.lower() :
        i = 1
        print("yes - without using in operator")
        break
    else :
        continue
if i == 0 :
    print("no - without using is operator")
i = len(names) - 1
while i >= 0 :
    print names[i]
    i -= 1
