# Write a python script to calculate HCF of two numbers
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
if a>b:
    min=b
else:
    min=a  
for i in range(1,min+1):
    if a%i==0 and b%i==0:
        hcf=i
print(hcf)