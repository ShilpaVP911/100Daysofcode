list1=[1,3,2,1]
if len(list1)%2!=0:
    print("not palindrome")
else:
    mid=len(list1)//2
    list2=list1[:mid]
    list3=list1[mid:]
    list3.reverse()
    if list2==list3:
        print("palindrome")
    else:
        print("not palindrome")