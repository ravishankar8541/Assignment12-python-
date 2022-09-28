# Write a python script to print first N prime numbers
n=int(input("Enter a number :"))
for a in range(2,n+1,1):
    count=0
    for b in range(1,a+1,1):
        if a%b==0:
            count+=1
    if count==2:
        print(a,end=" ")        