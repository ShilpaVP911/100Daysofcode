list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
low=0
high=len(list)-1
key=11
while low<=high:
    mid=(low+high)//2
    if list[mid]==key:
        print("Element found at index:", mid)
        break
    elif key < list[mid]:
        high=mid-1
    elif key > list[mid]:
        low=mid+1
    else:
        print("Element not found")
        break