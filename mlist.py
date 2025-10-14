list1=[2,4,6,8,10]
list2=[1,3,5,7,9]
i=j=0
mergedlist=[]
while i<len(list1) and j<len(list2):
    if list1[i]<list2[j]:
        mergedlist.append(list1[i])
        i+=1
    else:
        mergedlist.append(list2[j])
        j+=1
mergedlist.extend(list1[i:])
mergedlist.extend(list2[j:])
print(mergedlist)