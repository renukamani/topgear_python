e_name = list()
e_id = list()
for i in range(10) :
    e_name.append(raw_input("enter the name of employee"))
    e_id.append(int(raw_input("enter the id of employee")))
print(e_name)
ind = int(raw_input("enter the index of employee u want to select"))
print(e_name[ind],e_id[ind])
print(e_name[3:8])
print(e_name[2:])
rep_times = int(raw_input("enter the number of times you want to repeat print"))
print(e_name*rep_times)
e = e_name + e_id
print(e)
for i in range(10) :
    print(e_name[i],e_id[i])
