list1 = [22,45,24,68,61,50]
list2 = [11,45,64,76,35,24]
list3 = [1,2,3,4,5,6,7,8]
sort_list1 = sorted(list1)
sort_list2 = sorted(list2)
sort_list3 = sorted(list3)
max_list = list()
min_list = list()
max_list.extend((sort_list1[-1],sort_list1[-2],sort_list2[-1],sort_list2[-2],sort_list3[-1],sort_list3[-2]))
print max_list
avg = sum(max_list)/len(max_list)
print avg
min_list.extend((sort_list1[1],sort_list1[0],sort_list2[1],sort_list2[0],sort_list3[1],sort_list3[0]))
print min_list
avg = sum(min_list)/len(min_list)
print avg
