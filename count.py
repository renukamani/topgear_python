i_fh = open("input.txt")
o_fh = open("output.txt","w")
lin_no = 1
for line in i_fh :
    line = line.strip()
    words = line.split()
    word_count = len(words)
    char_count = 0
    for word in words :
        char_count = char_count + len(word)
    o_fh.write("No. of words in line "+str(lin_no)+" is: "+str(word_count)+"\n")
    o_fh.write("No. of characters in line "+str(lin_no)+" is: "+str(char_count)+"\n")
    lin_no = lin_no + 1
