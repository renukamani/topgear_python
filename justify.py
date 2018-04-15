import sys
def justify(line,width) :
    line = line.strip()
    act_len = len(line)
    spaces = width - act_len
    words = line.split()
    wrds_len = len(words)
    sp = int(spaces / (wrds_len - 1))
    ex_sp = spaces % (wrds_len - 1)
    lst = list()
    for i in range(len(words)) :
        lst.append(words[i])
        if i == (len(words) - 1) :
            break
        if i < ex_sp :
            lst.append(2 + sp)
        else :
            lst.append(1+sp)
    return lst

n = sys.argv
file = n[1]
width =int(n[2])
fh = open(file)
for line in fh :
    lst = justify(line,width)
    for item in lst :
        if type(item) is int :
            sys.stdout.write(" "*item)
        else :
            sys.stdout.write(item)
    sys.stdout.write("\n")
