# Write a python script to calculate LCM of two numbers
n1=int(input("Enter the first number :"))
n2=int(input("Enter the second number :"))
if n1>n2:
    max=n1
else:
    max=n2
while(1):
    if max%n1==0 and max%n2==0:
        print("LCM =",max)
        break
    max+=1    
