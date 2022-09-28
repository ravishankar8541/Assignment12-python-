# Write a python script to print all Prime numbers under 100
n=2
while n<100:
    i=1
    count=0
    while i<=n:
        if n%i==0:
            count+=1   
        i+=1    
    if count==2:
        print(n,end=" ")   
    n+=1      
    
    
