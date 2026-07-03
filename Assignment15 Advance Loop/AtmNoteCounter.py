# 8.

#  ATM Note Counter


# A bank ATM dispenses ₹100 notes.


# Write a program to:


# - Read withdrawal amount

# - Count how many ₹100 notes needed using loop


# Input:

# 700


# Output:

# Notes = 7

 
no=int(input("enter the no"))
count=0
for i in range(no//100):
    no=no-100
    count=count+1
    if no==0:
       break
print("count",count)