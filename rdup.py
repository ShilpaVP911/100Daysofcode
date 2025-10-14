l1=[6,1,2,4,4,3,5]
newlist=[]
for i in l1:
    if i not in newlist:
        newlist.append(i)
print(newlist)
snewlist=sorted(newlist)
print(snewlist)