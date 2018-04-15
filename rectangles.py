import sys
arg = sys.argv

def intersection(x,y) :
    a_tl_x = x[0][0]
    a_tl_y = x[0][1]
    a_br_x = x[1][0]
    a_br_y = x[1][1]
    b_tl_x = y[0][0]
    b_tl_y = y[0][1]
    b_br_x = y[1][0]
    b_br_y = y[1][1]
    if (a_tl_x<b_tl_x) and (b_tl_x<a_br_x) and (a_tl_y<b_br_y)and (b_br_y<a_br_y) :
        z = [(b_tl_x,a_tl_y),(a_br_x,b_br_y)]
        return z
    elif (b_tl_x<a_tl_x) and (a_tl_x<b_br_x) and (b_tl_y<a_br_y)and (a_br_y<b_br_y) :
        z = [(a_tl_x,b_tl_y),(b_br_x,a_br_y)]
        return z
a = list()
b = list()
i =1
while i<len(arg) :
    if i<= 4 :
        a.append((arg[i],arg[i+1]))
    else :
        b.append((arg[i],arg[i+1]))
    i = i+2

c = intersection(a,b)
print(c)
