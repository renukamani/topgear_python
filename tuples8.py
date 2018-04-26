
def print_tup(tup) :
    for item in tup:
        print(item)
tup1 = (12,45,32,"python",75,2,"renu",57,24,97,54)
tup2 = tup1[4:]
print_tup(tup1)
print_tup(tup2)
rows = (("")*5)*5
for row in rows :
    print id(row)
tup3 = (5,3,7,1)
new_tup = tup1+tup3
print_tup(new_tup)
