# Merge two sorted linked lists so that the resulting linked list is also sorted.

list1 = [1,3,5,6,7,8,9,9]
list2 = [0,4,5,5,7,8,10,11]

for v2 in list2:
    for v1 in range(len(list1)):
        if v2>=list1[v1]:
            if v1 == len(list1)-1:
                list1 += [v2]
            continue
        else:
            list1 = list1[:v1] + [v2] + list1[v1:]
            break
            
print(list1)

