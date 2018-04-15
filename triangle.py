import sys
n = sys.argv
n = int(n[1])
r = n
c = n+(n-1)
Matrix = [[0 for x in range(c)] for y in range(r)]
while r > 0 :
    c = n+(n-1)
    if r == n :
        Matrix[r-1][int((c-1)/2)] = 1
        r = r-1
        continue
    while c > 0 :
        if c == 1 :
            Matrix[r-1][0] = Matrix[r][1]
        elif c == (2*n-1) :
            Matrix[r-1][c-1] = Matrix[r][c-2]
        else :
            Matrix[r-1][c-1] = Matrix[r][c-2] + Matrix[r][c]
        c = c-1
    r = r-1

for row in Matrix :
    for col in row :
        if col == 0 :
            col = " "
        else :
            col = str(col)
        sys.stdout.write(col)
    sys.stdout.write("\n")
