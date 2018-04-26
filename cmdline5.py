import sys
lst = sys.argv
lst.pop(0)
for item in lst :
    print item
if len(lst) == 3 :
    print(max(lst))
