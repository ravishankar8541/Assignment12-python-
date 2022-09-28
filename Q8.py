# Write a python script to print first N terms of a Fibonacci series
from tempfile import tempdir


a=1
b=1
temp=0
n=int(input("Enter a number :"))
i=1
print(a)
while i<=n:
   temp=a+b
   print(temp)
   a=b
   b=temp
   i+=1

