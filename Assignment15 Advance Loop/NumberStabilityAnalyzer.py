# 5.Number Stability Analyzer


# A science lab studies whether digits are in increasing order.


# Write a program using for-else loop:


# - If every next digit is greater than previous print Stable Number

# - Else Unstable Number


# Input:

# 12359


# Output:

# Stable Number



n=int(input("Enter the numebr : "))
n1=n
pre=n%10
n=n//10
while n>0:
    next=n%10
    if next>=pre:
        print("Unstable number ")
        break
    pre=n%10
    n=n//10
else:
    print("Stable Number")    