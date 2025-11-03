time_str = input("Enter the time string ")
hour= int(time_str[0:2])
minute= int(time_str[3:5])
second= int(time_str[6:8])
if second>=60:
    minute=minute+1
    second=second-60
if minute>=60:
    hour=hour+1
    minute=minute-60
if hour>=24:
    hour=hour-24
print(f"Corrected time string is {hour:02}:{minute:02}:{second:02}")