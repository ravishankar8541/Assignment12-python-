# Write a python script to reverse a number.
n=7867
r=0
while n!=0:
    rem=n%10
    r=r*10+rem
    n=n//10
print(r)
    
