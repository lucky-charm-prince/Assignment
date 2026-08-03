# 9.
# Abundant Number Detector

# A financial system analyzes surplus numbers.

# An Abundant Number:
# Sum of proper factors > number

# Write a program to check Abundant Number.

# Input:
# 12

# Output:
# Abundant Number

n=int(input("Enter the number : "))

count=0
if n>0:
    count=1
for i  in range(2,n//2+1):
    if n%i==0:
        count+=i

if count>n:
    print("Abundant Number")
else:
    print("Not ABudent Number")    
