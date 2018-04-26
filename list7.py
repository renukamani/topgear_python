
def print_lst(lst) :
    for item in lst:
        print(item)
lst1 = [12,45,32,56,75,24,57,24,97,54]
lst2 = lst1[4:9]
print_lst(lst1)
print_lst(lst2)
rows = [[""]*5]*5
for row in rows :
    print id(row)
lst3 = [5,3,7,1]
new_lst = lst1+lst3
print_lst(new_lst)
