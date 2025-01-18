#Take a number input from the user and check if it is prime
number=int(input("enter the number"))
flag=False
from math import sqrt
for i in range(2,int(sqrt (number))+1):
    if number%i==0:
        flag=True
       
        break
if flag :
    print(number,"is not prime")
else:
        print(number,"is a prime number")



