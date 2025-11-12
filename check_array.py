array=list(map(int, input("Enter array elements separated by spaces: ").split()))
sorted_array=sorted(array)
print("Sorted array in ascending order:", sorted_array)
rev_array=sorted_array[::-1]
print("Sorted array in descending order:", rev_array)
if array==sorted(array):
    print("The array is sorted in ascending order.")
elif array==rev_array:
    print("The array is sorted in descending order.")
else:
    print("The array is not sorted.")

