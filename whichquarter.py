month= int(input("Enter the month"))
if month in range(1,4):
    print("First Quarter")
elif month in range(4,7):
    print("Second Quarter")
elif month in range(7,10):
    print("Third Quarter")
elif month in range(10,13):
    print("Fourth Quarter")
else:
    print("Invalid Month")