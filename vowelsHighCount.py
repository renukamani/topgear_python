from string import punctuation

def getSecond(elem) :
    return elem[1]

fh = open("sample_topgear.txt")
vowels = "aeiouAEIOU"
count = dict()
for line in fh :
    line = line.strip()
    words = line.split()
    for word in words :
        word = word.strip(punctuation)
        for letter in word :
            if letter in vowels :
                count[word] = count.get(word,0) + 1

            else :
                continue

max_count = max(count.items(), key = getSecond)[1]

for k,v in count.items() :
    if v == max_count :
        print(v,k)
