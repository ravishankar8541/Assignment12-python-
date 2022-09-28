""" Write a python script to print all Prime numbers between two given numbers (both
values inclusive)"""
lower_value=int(input("Enter lower value "))
upper_value=int(input("Enter upper value "))
for a in range(lower_value,upper_value+1,1):
    count=0
    for b in range(1,a+1,1):
        if a%b==0:
            count+=1
    if count==2:
        print(a,end=" ")        
