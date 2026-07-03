"""2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4"""

a,b=map(int,(input("enter the no=").split()))
count=0
"""
for i in range(a,b+1):
    if i%7==0:
        count=count+1
print("the no counts are=",count) """

count=0
while a<=b:
    if a%7==0:
       count=count+1
    a=a+1

print("the counts are=",count)
    