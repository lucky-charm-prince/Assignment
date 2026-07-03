# 4.
# Armstrong Number Finder

# A digital number analysis system checks for Armstrong numbers within a range.
# The user enters starting and ending numbers.
# The system finds all Armstrong numbers using nested loops.

# Input:
# Enter starting number: 1
# Enter ending number: 500

# Output:
# Armstrong Numbers are:
# 1
# 153
# 370
# 371
# 407

x=int(input("Enter the number : "))
y=int(input("Enter the number : "))


for i in range(x,y+1):
    digits=len(str(i))
    n=i
    sum=0
    while n>0:
        d=n%10
        sum=d**digits+sum
        n=n//10
    if i==sum:
        print(i)    
 