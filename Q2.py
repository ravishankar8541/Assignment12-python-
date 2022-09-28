# Write a python script to check whether a given number is Prime or not
n=22
i=2
count=0;
while i<=n//2:
    if n%i==0:
        count+=1
        if count==1:
            print("Not Prime number")
            break
    i+=1
else:
    print("prime number")          

 