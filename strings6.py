str1 = raw_input("enter the string")
for letter in str1 :
    print letter
print(str1*100)
str2 = raw_input("enter a string with <:> character ")
str2_1 = str2[:str2.index(":")]
str2_2 = str2[str2.index(":")-1:]
print str2_1
print str2_2
str3 = raw_input("enter the string u want to concatenate with "+ str1)
new_str = str1+str3
print new_str
