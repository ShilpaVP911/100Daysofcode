arr=[1, 2, 3, 4, 5,1,3,4,6,1,]
num=int(input("Enter the number to find its occurrences: "))
count=0
for i in arr:
    if i==num:
        count+=1
print(f"The number {num} occurs {count} times in the array.")


arr1=[10, 20, 30, 40, 50 ,10,20,30,40,10]
num1=int(input("Enter the number to find its occurrences: "))
count1=0
count1=arr1.count(num1)

print(f"The number {num1} occurs {count1} times in the array.")