import math
num= int(input("Enter the number:"))

p=0;
if ( num==1) :
    p=1

while num%2==0:
    p=2
    num=num/2

for i in range(3,int(math.sqrt(num))+1,2):
    while num%i==0:
        p=i
        num=num/i

if num>2:
    p=num

print("The largest prime factor is :",int (p))