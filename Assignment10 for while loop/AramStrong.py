# 6. Armstrong Number (3-digit)
# In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
# Write a program to *check whether a number is an Armstrong number using loops*.

# Input: 153
# Output: Armstrong
 
n=int(input("Enter the three digit number : "))
temp=n
total=0


# using the for loop
# for i in range(len(str(n))):
#     x=n%10
#     total+=x*x*x
#     n=n//10
# if temp==total:
#     print("Aram Strong number")    
# else:
#     print("Not a aram Strong number")    




while n>0:
    x=n%10
    total+=x*x*x
    n=n//10
if temp==total:
    print("Aram Strong number")    
else:
    print("Not a aram Strong number")    
